"""
Conversión y análisis de audio.
"""

import subprocess
import wave
from pathlib import Path


def convertir_a_wav_16k(input_file: Path, output_file: Path):
    """
    Convierte audio/video a WAV mono 16k PCM.
    """

    comando = [
        "ffmpeg",
        "-y",
        "-i",
        str(input_file),
        "-ac",
        "1",
        "-ar",
        "16000",
        "-vn",
        "-acodec",
        "pcm_s16le",
        str(output_file)
    ]

    proceso = subprocess.run(
        comando,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if proceso.returncode != 0:
        raise RuntimeError(
            f"FFmpeg error:\n{proceso.stderr}"
        )


def obtener_duracion_wav(ruta_wav: Path) -> float:
    """
    Obtiene duración del WAV.
    """

    with wave.open(str(ruta_wav), "rb") as wf:
        frames = wf.getnframes()
        rate = wf.getframerate()

        return frames / float(rate)