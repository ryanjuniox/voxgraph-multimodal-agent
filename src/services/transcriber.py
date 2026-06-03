import numpy as np
import mlx_whisper


DEFAULT_MODEL = "mlx-community/whisper-large-v3-mlx"


def transcribe(audio: np.ndarray, language: str = "pt") -> dict:
    """Transcreve um numpy array de áudio usando mlx_whisper.

    Parameters
    ----------
    audio : np.ndarray
        Waveform do áudio em float32, mono.
    language : str
        Idioma do áudio (padrão: português).

    Returns
    -------
    dict
        Resultado da transcrição contendo text, segments e language.
    """
    result = mlx_whisper.transcribe(
        audio,
        path_or_hf_repo=DEFAULT_MODEL,
        language=language,
    )

    return result
