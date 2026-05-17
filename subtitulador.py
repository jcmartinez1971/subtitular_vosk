"""
Subtitulador profesional offline usando VOSK.
"""

import argparse
import tempfile
import shutil

from pathlib import Path
from rich.console import Console

from utilidades import validar_archivo
from audio_utils import (
    convertir_a_wav_16k,
    obtener_duracion_wav
)
from transcriptor import TranscriptorVosk
from generador_srt import GeneradorSRT
from diagnostico_transcripcion import (
    mostrar_estadisticas
)

console = Console()


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "archivo",
        help="Ruta del audio/video"
    )

    parser.add_argument(
        "--modelo",
        required=True,
        help="Ruta modelo VOSK"
    )

    args = parser.parse_args()

    archivo = Path(args.archivo)
    modelo = Path(args.modelo)

    validar_archivo(archivo)

    temp_dir = Path(tempfile.mkdtemp())

    try:

        wav_temp = temp_dir / "audio.wav"

        console.print(
            "[cyan][INFO][/cyan] Extrayendo audio..."
        )

        convertir_a_wav_16k(
            archivo,
            wav_temp
        )

        duracion = obtener_duracion_wav(
            wav_temp
        )

        transcriptor = TranscriptorVosk(
            modelo
        )

        console.print(
            "[cyan][INFO][/cyan] Transcribiendo..."
        )

        resultados, tiempo_total = (
            transcriptor.transcribir(wav_temp)
        )

        salida_srt = archivo.with_suffix(".srt")

        generador = GeneradorSRT()

        segmentos = generador.generar(
            resultados,
            salida_srt
        )

        mostrar_estadisticas(
            duracion,
            tiempo_total,
            segmentos
        )

        console.print(
            f"[green][OK][/green] Archivo: {salida_srt}"
        )

    finally:

        shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    main()