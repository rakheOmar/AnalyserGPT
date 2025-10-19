from autogen_agentchat.agents import AssistantAgent

from agents.prompts.data_analyzer_prompt import DATA_ANALYZER_PROMPT


def get_data_analyzer_agent(model_client):
    data_analyzer_agent = AssistantAgent(
        name="Data_Analyzer_Agent",
        description="An agent which helps with solving Data Analysis task and gives the code as well",
        model_client=model_client,
        system_message=DATA_ANALYZER_PROMPT,
    )

    return data_analyzer_agent
