from src.services.transcriber import transcribe
from src.utils.audio import bytes_to_numpy


def run(audio_bytes: bytes) -> str:
    """Pipeline de processamento de áudio.

    Define o fluxo: bytes → numpy → transcrição.

    Parameters
    ----------
    audio_bytes : bytes
        Bytes brutos do áudio capturado.

    Returns
    -------
    str
        Texto transcrito.
    """
    # TODO Fazer o pipeline propriamente para o TranscriberAgent
    audio_array = bytes_to_numpy(audio_bytes)
    result = transcribe(audio_array)

    return result["text"]
