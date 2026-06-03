from pydantic import BaseModel


class RequestState(BaseModel):
    question: str = ""
    answer: str = ""
    request_type: str = ""  # audio or text
    audio_bytes: bytes | None = None
