from src.agent.agent_builder import build_agent
from src.utils.logger import logging
from src.utils.constants import MODEL_ANSWER_GENERATOR
from .prompt import PROMPT_ANSWER_GENERATOR


class AnswerGenerator:
    def __init__(self):
        self.agent = build_agent(
            model_name=MODEL_ANSWER_GENERATOR, prompt=PROMPT_ANSWER_GENERATOR
        )

    def run(self, question: str):
        logging.info("Running answer generator agent for question: %s", question)

        try:
            response = self.agent.run_sync(question)
            logging.info("Answer generated successfully")
        except Exception as e:
            logging.error("Error running answer generator agent: %s", str(e))
            raise
        return response.output

    def answer_generator(self, state: dict) -> dict:
        question = state.question
        logging.info("Answer generator node started | Question: %s", question)
        answer = self.run(question)
        logging.info("Answer generator node completed")
        return {"answer": answer}
