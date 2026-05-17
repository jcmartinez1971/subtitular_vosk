"""
Motor principal de transcripción VOSK.
"""

import json
import wave
import time

from pathlib import Path
from vosk import Model, KaldiRecognizer
from rich.console import Console
from tqdm import tqdm

console = Console()


class TranscriptorVosk:
    """
    Transcriptor offline usando VOSK.
    """

    def __init__(self, modelo_path: Path):

        if not modelo_path.exists():
            raise FileNotFoundError(
                f"Modelo no encontrado: {modelo_path}"
            )

        console.print("[cyan][INFO][/cyan] Cargando modelo VOSK...")

        self.modelo = Model(str(modelo_path))

    def transcribir(self, wav_path: Path):

        resultados = []

        with wave.open(str(wav_path), "rb") as wf:

            recognizer = KaldiRecognizer(
                self.modelo,
                wf.getframerate()
            )

            recognizer.SetWords(True)

            total_frames = wf.getnframes()

            chunk_size = 4000

            inicio = time.time()

            with tqdm(
                total=total_frames,
                desc="Transcribiendo",
                unit="frames"
            ) as barra:

                while True:

                    data = wf.readframes(chunk_size)

                    if len(data) == 0:
                        break

                    if recognizer.AcceptWaveform(data):

                        resultado = json.loads(
                            recognizer.Result()
                        )

                        resultados.append(resultado)

                    barra.update(chunk_size)

            final = json.loads(recognizer.FinalResult())

            resultados.append(final)

            tiempo_total = time.time() - inicio

        return resultados, tiempo_total