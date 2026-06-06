from .prompt import PROMPT_TRANSCRIBER

from src.utils.logger import logging
from src.utils.constants import MODEL_TRANSCRIBER_AGENT, OLLAMA_BASE_URL
from src.tools.deps_context import ContextTools
from src.tools.transcription_tool import speech_to_text

from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider


class TranscriberAgent:
    def __init__(self):
        self.model = OllamaModel(
            MODEL_TRANSCRIBER_AGENT, provider=OllamaProvider(base_url=OLLAMA_BASE_URL)
        )

    def _run(self, audio_bytes: bytes) -> str:
        logging.info(
            "Running transcriber agent | Audio bytes size: %d", len(audio_bytes)
        )
        agent = Agent(
            model=self.model,
            tools=[speech_to_text],
            system_prompt=PROMPT_TRANSCRIBER,
            deps_type=ContextTools,
        )
        deps = ContextTools(audio_bytes=audio_bytes, question="", answer="")
        try:
            transcription = agent.run_sync(
                "Transcribe the following audio file.", deps=deps
            )
            logging.info("Transcription completed and corrected successfully")
            return transcription.output
        except Exception as e:
            logging.error("Error in transcriber agent: %s", e)
            raise Exception(f"Error in transcriber agent: {e}")

    def transcriber_agent(self, state: dict) -> dict:
        logging.info("Transcriber node started")
        audio_bytes = state.audio_bytes
        corrected_text = self._run(audio_bytes)
        logging.info("Transcriber node completed | Corrected text: %s", corrected_text)
        return {"question": corrected_text}
