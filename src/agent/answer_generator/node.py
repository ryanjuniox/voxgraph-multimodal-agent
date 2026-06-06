from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider

from src.utils.logger import logging
from src.utils.constants import OLLAMA_BASE_URL, MODEL_ANSWER_GENERATOR
from .prompt import PROMPT_ANSWER_GENERATOR


class AnswerGenerator:
    def __init__(self):
        self.model = OllamaModel(
            MODEL_ANSWER_GENERATOR, provider=OllamaProvider(base_url=OLLAMA_BASE_URL)
        )

    def _run(self, question: str):
        logging.info("Running answer generator agent for question: %s", question)
        agent = Agent(
            self.model, system_prompt=PROMPT_ANSWER_GENERATOR, output_type=str
        )

        try:
            response = agent.run_sync(question)
            logging.info("Answer generated successfully")
        except Exception as e:
            logging.error("Error running answer generator agent: %s", str(e))
            raise
        return response.output

    def answer_generator(self, state: dict) -> dict:
        question = state.question
        logging.info("Answer generator node started | Question: %s", question)
        answer = self._run(question)
        logging.info("Answer generator node completed")
        return {"answer": answer}
