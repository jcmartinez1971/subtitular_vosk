"""
Generador profesional de archivos SRT.
"""

from pathlib import Path
from utilidades import formatear_timestamp


class GeneradorSRT:
    """
    Construye subtítulos SRT.
    """

    def __init__(self, max_palabras=12):

        self.max_palabras = max_palabras

    def generar(self, resultados, output_srt: Path):

        segmentos = []

        palabras_actuales = []

        inicio = None
        fin = None

        for bloque in resultados:

            if "result" not in bloque:
                continue

            for palabra in bloque["result"]:

                if inicio is None:
                    inicio = palabra["start"]

                fin = palabra["end"]

                palabras_actuales.append(
                    palabra["word"]
                )

                if len(palabras_actuales) >= self.max_palabras:

                    segmentos.append({
                        "inicio": inicio,
                        "fin": fin,
                        "texto": " ".join(palabras_actuales)
                    })

                    palabras_actuales = []
                    inicio = None

        if palabras_actuales:

            segmentos.append({
                "inicio": inicio,
                "fin": fin,
                "texto": " ".join(palabras_actuales)
            })

        with open(output_srt, "w", encoding="utf-8") as archivo:

            for idx, seg in enumerate(segmentos, start=1):

                archivo.write(f"{idx}\n")

                archivo.write(
                    f"{formatear_timestamp(seg['inicio'])} "
                    f"--> "
                    f"{formatear_timestamp(seg['fin'])}\n"
                )

                archivo.write(f"{seg['texto']}\n\n")

        return len(segmentos)