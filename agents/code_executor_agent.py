import asyncio

from autogen_agentchat.agents import CodeExecutorAgent
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor


def get_code_executor_agent(code_executor):
    return CodeExecutorAgent(name="CodeExecutor", code_executor=code_executor)


async def main():
    docker = DockerCommandLineCodeExecutor(work_dir="temp", timeout=120)
    code_executor_agent = get_code_executor_agent(docker)

    task = TextMessage(
        content=(
            """
            Here is the Python code you have to run.
            ```python
            print('Hello Wooooooooorld')
            ```
            """
        ),
        source="User",
    )

    try:
        await docker.start()
        res = await code_executor_agent.on_messages(
            messages=[task],
            cancellation_token=CancellationToken(),
        )
        print("Result is:", res)
    except Exception as e:
        print("Error:", e)
    finally:
        await docker.stop()


if __name__ == "__main__":
    asyncio.run(main())
