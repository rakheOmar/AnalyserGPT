import asyncio
from pathlib import Path

import streamlit as st
from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import TextMessage

from config.docker_util import (
    getDockerCommandLineExecutor,
    start_docker_container,
    stop_docker_container,
)
from models.model_client import get_model_client
from teams.analyzer_team import get_data_analyzer_team

st.set_page_config(
    page_title="Data Analyzer AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("📊 Data Analyzer AI")

with st.sidebar:
    st.header("Configuration")

    st.subheader("Upload CSV")
    uploaded_file = st.file_uploader("Choose file", type="csv")

    if uploaded_file is not None:
        file_path = Path("temp") / uploaded_file.name
        file_path.parent.mkdir(exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"✓ {uploaded_file.name}")

        with st.expander("Preview"):
            try:
                import pandas as pd

                df = pd.read_csv(file_path)
                st.dataframe(df.head(10))
                st.caption(f"{len(df)} rows × {len(df.columns)} cols")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.info("Upload CSV to begin")

    st.divider()

    st.subheader("Analysis Request")
    user_prompt = st.text_area(
        "Describe your analysis",
        placeholder="Analyze patterns and create visualizations...",
        height=100,
    )

    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        generate_plots = st.checkbox("Plots", value=True)
    with col2:
        save_summary = st.checkbox("Summary", value=True)

    st.divider()

    run_analysis = st.button(
        "Run Analysis",
        type="primary",
        use_container_width=True,
        disabled=(uploaded_file is None or not user_prompt.strip()),
    )


if run_analysis and uploaded_file is not None and user_prompt.strip():
    task_components = [f"Analyze {uploaded_file.name}.", user_prompt.strip()]

    if generate_plots:
        task_components.append("Generate visualizations as PNG files.")

    if save_summary:
        task_components.append("Provide summary in summary.md.")

    final_task = " ".join(task_components)

    st.header("Analysis")

    output_placeholder = st.empty()
    messages_container = st.container()

    with messages_container:
        st.subheader("Agent Activity")
        messages_placeholder = st.empty()

    async def run_analysis_async():
        openai_model_client = get_model_client()
        docker = getDockerCommandLineExecutor()
        team = get_data_analyzer_team(docker, openai_model_client)

        messages_log = []

        try:
            await start_docker_container(docker)

            with output_placeholder.container():
                st.info("⏳ Running...")

            async for message in team.run_stream(task=final_task):
                if isinstance(message, TextMessage):
                    source = message.source
                    content = message.content

                    print(f"\n{'=' * 60}")
                    print(f"[{source}]")
                    print(f"{content}")
                    print(f"{'=' * 60}\n")

                    if "CodeExecutor" in source:
                        color_func = st.success
                        emoji = "🟢"
                    elif "Data" in source:
                        color_func = st.info
                        emoji = "🔵"
                    else:
                        color_func = st.error
                        emoji = "🔴"

                    messages_log.append(
                        {
                            "source": source,
                            "content": content,
                            "color_func": color_func,
                            "emoji": emoji,
                        }
                    )

                    with messages_placeholder.container():
                        for msg in messages_log:
                            msg["color_func"](
                                f"**{msg['emoji']} {msg['source']}**\n\n{msg['content']}"
                            )

                elif isinstance(message, TaskResult):
                    with output_placeholder.container():
                        st.success("✓ Complete")
                        st.caption(f"Stop: {message.stop_reason}")

            st.subheader("Generated Files")
            temp_dir = Path("temp")
            output_files = list(temp_dir.glob("*"))
            if uploaded_file:
                output_files = [f for f in output_files if f.name != uploaded_file.name]

            if output_files:
                for file in output_files:
                    if file.is_file():
                        st.write(f"📄 {file.name}")

                        if file.suffix in [".md", ".txt", ".csv"]:
                            with st.expander(f"View {file.name}"):
                                with open(file, "r") as f:
                                    st.text(f.read())

                        elif file.suffix in [".png", ".jpg", ".jpeg"]:
                            with st.expander(f"View {file.name}"):
                                st.image(str(file))
            else:
                st.info("No additional files.")

        except Exception as e:
            st.error(f"Error: {str(e)}")
            print(f"\n[ERROR] {str(e)}\n")

        finally:
            await stop_docker_container(docker)

    try:
        asyncio.run(run_analysis_async())
    except Exception as e:
        st.error(f"Failed: {str(e)}")

else:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Quick Start
        
        1. Upload CSV file
        2. Enter analysis request
        3. Run analysis
        4. View results
        """)

    with col2:
        st.markdown("""
        ### Features
        
        - Real-time streaming
        - Auto CSV handling
        - Multi-format output
        - AI-powered analysis
        """)

    if uploaded_file is None:
        st.info("👈 Upload CSV to begin")
    elif not user_prompt.strip():
        st.info("👈 Enter analysis request")
    else:
        st.success("Ready! Click Run Analysis")

st.divider()
st.markdown(
    "<div style='text-align: center; color: gray; font-size: 12px;'>Data Analyzer AI</div>",
    unsafe_allow_html=True,
)
