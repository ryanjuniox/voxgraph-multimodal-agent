from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider

from src.utils.logger import logging
from src.utils.constants import OLLAMA_BASE_URL


def _build_model(model: str):
    provider, name_model = model.split("/", maxsplit=1)
    if provider == "ollama":
        return OllamaModel(
            name_model, provider=OllamaProvider(base_url=OLLAMA_BASE_URL)
        )
    else:
        logging.error(f"Unknown provider: {provider}")
        raise ValueError(f"Unknown provider: {provider}")


def build_agent(
    model_name: str, prompt: str, tools: list = [], deps_type=None
) -> Agent:
    model = _build_model(model=model_name)
    agent = Agent(
        model=model,
        tools=tools,
        system_prompt=prompt,
        deps_type=deps_type,
    )
    return agent
