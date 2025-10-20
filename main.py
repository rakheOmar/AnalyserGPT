import asyncio

from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import TextMessage

from config.docker_util import (
    getDockerCommandLineExecutor,
    start_docker_container,
    stop_docker_container,
)
from models.model_client import get_model_client
from teams.analyzer_team import get_data_analyzer_team


async def main():
    openai_model_client = get_model_client()
    docker = getDockerCommandLineExecutor()

    team = get_data_analyzer_team(docker, openai_model_client)

    try:
        task = "Can you analyze the titanic.csv dataset, generate a graph of survived and died passengers grouped by class, and save it as output.png? Additionally, provide a summary of the survival rate for each class in a text file named summary.md"

        await start_docker_container(docker)

        async for message in team.run_stream(task=task):
            print("=" * 40)
            if isinstance(message, TextMessage):
                print(message.source, ":", message.content)

            elif isinstance(message, TaskResult):
                print("Stop Reason :", message.stop_reason)
    
    except Exception as e:
        print(e)
    finally:
        await stop_docker_container(docker)


if __name__ == "__main__":
    asyncio.run(main())
