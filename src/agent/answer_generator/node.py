from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider

from src.utils.constants import OLLAMA_BASE_URL, MODEL_ANSWER_GENERATOR
from .prompt import PROMPT_ANSWER_GENERATOR


class AnswerGenerator:
    def __init__(self):
        self.model = OllamaModel(
            MODEL_ANSWER_GENERATOR, provider=OllamaProvider(base_url=OLLAMA_BASE_URL)
        )

    def _run(self, question: str):
        agent = Agent(
            self.model, system_prompt=PROMPT_ANSWER_GENERATOR, output_type=str
        )

        response = agent.run_sync(question)
        return response.output

    def answer_generator(self, state: dict) -> dict:
        question = state["question"]
        answer = self._run(question)
        return {"answer": answer}
