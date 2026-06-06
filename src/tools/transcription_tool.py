from .deps_context import ContextTools

from src.services.transcriber import transcribe
from src.utils.audio import bytes_to_numpy

from pydantic_ai import RunContext


def speech_to_text(ctx: RunContext[ContextTools]) -> str:
    """Transcribe raw audio bytes into text.

    Converts the audio bytes from the context into a NumPy waveform,
    runs speech-to-text transcription, and returns the raw transcribed text.
    """
    audio_bytes = ctx.deps.audio_bytes
    audio_array = bytes_to_numpy(audio_bytes)
    audio_transcription = transcribe(audio_array)
    return audio_transcription["text"]
