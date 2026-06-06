from dataclasses import dataclass


@dataclass
class ContextTools:
    audio_bytes: bytes
    question: str
    answer: str
