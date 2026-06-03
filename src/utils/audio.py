import io

import numpy as np
import soundfile as sf


def bytes_to_numpy(audio_bytes: bytes) -> np.ndarray:
    """Converte bytes de áudio em um numpy array float32 mono.

    Parameters
    ----------
    audio_bytes : bytes
        Bytes brutos do arquivo de áudio (WAV, FLAC, OGG, etc.)

    Returns
    -------
    np.ndarray
        Waveform do áudio em float32, canal mono.
    """
    audio_data, _ = sf.read(io.BytesIO(audio_bytes))

    # Converte stereo para mono se necessário
    if audio_data.ndim > 1:
        audio_data = audio_data.mean(axis=1)

    return audio_data.astype(np.float32)
