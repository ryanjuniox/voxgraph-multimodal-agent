from .deps_context import ContextTools

from src.services.transcriber import transcribe
from src.utils.audio import bytes_to_numpy
from src.utils.logger import logging

from pydantic_ai import RunContext


def speech_to_text(ctx: RunContext[ContextTools]) -> str:
    """Transcribe raw audio bytes into text.

    Converts the audio bytes from the context into a NumPy waveform,
    runs speech-to-text transcription, and returns the raw transcribed text.
    """
    audio_bytes = ctx.deps.audio_bytes
    logging.info("speech_to_text called | audio_bytes length: %d", len(audio_bytes))
    audio_array = bytes_to_numpy(audio_bytes)
    logging.info("audio_array shape: %s", audio_array.shape)
    audio_transcription = transcribe(audio_array)
    logging.info("transcription result: %s", audio_transcription)
    return audio_transcription["text"]
