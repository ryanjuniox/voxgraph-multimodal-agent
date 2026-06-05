from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider

from src.utils.constants import OLLAMA_BASE_URL, MODEL_ANSWER_GENERATOR


class AnswerGenerator:
    def __init__(self):
        self.model = OllamaModel(
            MODEL_ANSWER_GENERATOR, provider=OllamaProvider(base_url=OLLAMA_BASE_URL)
        )

    def answer_generator(self, state: dict) -> dict:
        # TODO Retorno agent
        pass
