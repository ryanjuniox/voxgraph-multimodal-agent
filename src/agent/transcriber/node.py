from .prompt import (
    PROMPT_TRANSCRIBER_SYSTEM,
    PROMPT_TRANSCRIBER_AUDIO,
    PROMPT_TRANSCRIBER_TEXT,
)

from src.utils.logger import logging
from src.utils.constants import MODEL_TRANSCRIBER_AGENT
from src.tools.deps_context import ContextTools
from src.tools.transcription_tool import speech_to_text
from src.agent.agent_builder import build_agent


class TranscriberAgent:
    def __init__(self):
        self.agent = build_agent(
            model_name=MODEL_TRANSCRIBER_AGENT,
            prompt=PROMPT_TRANSCRIBER_SYSTEM,
            tools=[speech_to_text],
            deps_type=ContextTools,
        )

    def _build_prompt(self, request_type: str, question: str = None) -> str:
        if request_type == "text":
            return PROMPT_TRANSCRIBER_TEXT.replace("{USER_INPUT}", question or "")
        return PROMPT_TRANSCRIBER_AUDIO

    def _run(self, state) -> str:
        request_type = state.request_type
        question = state.question if hasattr(state, "question") else None

        deps = None
        if request_type == "audio":
            audio_bytes = state.audio_bytes
            if not audio_bytes:
                raise ValueError("Audio bytes are required for transcription")
            deps = ContextTools(audio_bytes=audio_bytes, question="", answer="")
            logging.info(
                "Running transcriber agent | Audio bytes size: %d", len(audio_bytes)
            )
        else:
            logging.info(
                "Running transcriber agent | Text mode | Question: %s", question
            )

        try:
            prompt = self._build_prompt(request_type=request_type, question=question)
            transcription = self.agent.run_sync(
                prompt,
                deps=deps,
                model_settings={"thinking": False},
            )
            logging.info("Transcription completed and corrected successfully")
            return transcription.output
        except Exception as e:
            logging.error("Error in transcriber agent: %s", e)
            raise Exception(f"Error in transcriber agent: {e}")

    def transcriber_agent(self, state) -> dict:
        logging.info("Transcriber node started")
        corrected_text = self._run(state=state)
        logging.info("Transcriber node completed | Corrected text: %s", corrected_text)
        return {"question": corrected_text}
