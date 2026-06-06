from .prompt import PROMPT_TRANSCRIBER

from src.utils.constants import MODEL_TRANSCRIBER_AGENT, OLLAMA_BASE_URL
from src.tools.deps_context import ContextTools
from src.tools.transcription_tool import transcriber

from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider


class TranscriberAgent:
    def __init__(self):
        self.model = OllamaModel(
            MODEL_TRANSCRIBER_AGENT, provider=OllamaProvider(base_url=OLLAMA_BASE_URL)
        )

    def _run(self, audio_bytes: bytes) -> str:
        agent = Agent(
            model=self.model,
            tools=[transcriber],
            system_prompt=PROMPT_TRANSCRIBER,
            deps_type=ContextTools,
        )
        deps = ContextTools(audio_bytes=audio_bytes, question="", answer="")
        transcription = agent.run_sync(
            "Transcribe the following audio file.", deps=deps
        )
        return transcription.output

    def transcriber_agent(self, state: dict) -> dict:
        audio_bytes = state.audio_bytes
        corrected_text = self._run(audio_bytes)
        return {"question": corrected_text}
