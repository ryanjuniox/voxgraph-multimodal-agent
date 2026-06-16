from .prompt import (
    PROMPT_TRANSCRIBER_SYSTEM,
    PROMPT_TRANSCRIBER_TEXT,
)

from src.utils.logger import logging
from src.utils.constants import MODEL_TRANSCRIBER_AGENT
from src.utils.audio import bytes_to_numpy
from src.agent.agent_builder import build_agent
from src.services.transcriber import transcribe


class MessageRefiner:
    def __init__(self):
        self.agent = build_agent(
            model_name=MODEL_TRANSCRIBER_AGENT,
            prompt=PROMPT_TRANSCRIBER_SYSTEM
        )
    
    def _transcriber_audio(self, audio_bytes: bytes) -> str:
        audio_array = bytes_to_numpy(audio_bytes)
        audio_transcription = transcribe(audio_array)
        return audio_transcription["text"]

    def _build_prompt(self, request_type: str, question: str = None) -> str:
        return PROMPT_TRANSCRIBER_TEXT.replace("{USER_INPUT}", question or "")

    def run(self, state) -> str: 
        audio_transcription = None
        request_type = state.request_type
        if request_type == "audio":
            audio_bytes = state.audio_bytes
            if not audio_bytes:
                raise ValueError("Audio bytes are required for transcription")
            audio_transcription = self._transcriber_audio(audio_bytes)
            logging.info(f"audio transcription: {audio_transcription}")
        else:
            logging.info(
                "Running transcriber agent | Text mode | Question: %s", state.question
            )

        if audio_transcription:
            state.question = audio_transcription
            logging.info(f"Question: {state.question}")

        try:
            prompt = self._build_prompt(request_type=request_type, question=state.question)
            logging.info(f"Prompt created successfully: {prompt}")
            reformulated_message = self.agent.run_sync(user_prompt=prompt)
            logging.info("Transcription completed and corrected successfully")
            return reformulated_message.output
        except Exception as e:
            logging.error("Error in MessageRefiner agent: %s", e)
            raise Exception(f"Error in MessageRefiner agent: {e}")

    def message_refiner(self, state) -> dict:
        logging.info("MessageRefiner node started")
        reformulated_message = self.run(state=state)
        return {"question": reformulated_message}
