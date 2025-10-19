import os

from autogen_ext.models.anthropic import AnthropicChatCompletionClient
from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv

load_dotenv()

OPEN_AI = os.getenv("OPENAI_API_KEY")
GEMINI = os.getenv("GEMINI_API_KEY")
OPEN_ROUTER = os.getenv("OPEN_ROUTER_API_KEY")
GROQ = os.getenv("GROQ_API_KEY")
ANTROPHIC = os.getenv("ANTROPHIC_API_KEY")

gemini_model_client = OpenAIChatCompletionClient(
    api_key=GEMINI,  # type: ignore
    model="gemini-2.5-flash",
    model_info={
        "vision": True,
        "function_calling": True,
        "json_output": False,
        "structured_output": False,
        "family": "gemini",
    },
)

open_router_model_client = OpenAIChatCompletionClient(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPEN_ROUTER,  # type: ignore
    model="mistralai/mistral-small-3.2-24b-instruct:free",
    model_info={
        "vision": True,
        "function_calling": True,
        "json_output": False,
        "structured_output": False,
        "family": "deepseek",
    },
)


anthropic_model_client = AnthropicChatCompletionClient(
    api_key=ANTROPHIC,  # type: ignore
    model="claude-3.5-sonnet-20240620",
    model_info={
        "vision": True,
        "function_calling": True,
        "json_output": False,
        "structured_output": False,
        "family": "anthropic",
    },
)


ollama_model_client = OllamaChatCompletionClient(
    model="phi4",
    model_info={
        "vision": True,
        "function_calling": True,
        "json_output": False,
        "structured_output": False,
        "family": "llama",
    },
)


def get_model_client():
    return ollama_model_client
