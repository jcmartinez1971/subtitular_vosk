"""
Funciones utilitarias generales.
"""

from pathlib import Path
from datetime import timedelta
from rich.console import Console

console = Console()


def formatear_timestamp(segundos: float) -> str:
    """
    Convierte segundos a formato SRT.
    """

    td = timedelta(seconds=segundos)

    total_segundos = int(td.total_seconds())

    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos_enteros = total_segundos % 60

    milisegundos = int((segundos - int(segundos)) * 1000)

    return (
        f"{horas:02}:{minutos:02}:{segundos_enteros:02},"
        f"{milisegundos:03}"
    )


def validar_archivo(ruta: Path):
    """
    Verifica existencia del archivo.
    """

    if not ruta.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {ruta}")


def crear_directorio(ruta: Path):
    """
    Crea directorio si no existe.
    """

    ruta.mkdir(parents=True, exist_ok=True)