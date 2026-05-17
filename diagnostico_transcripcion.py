"""
Herramientas de diagnóstico y rendimiento.
"""

from rich.console import Console

console = Console()


def mostrar_estadisticas(
    duracion,
    tiempo_total,
    segmentos
):
    """
    Muestra estadísticas finales.
    """

    velocidad = duracion / tiempo_total

    console.print("\n[green][OK][/green] Subtítulos generados")

    console.print(f"Duración media: {duracion:.2f} s")
    console.print(f"Tiempo procesamiento: {tiempo_total:.2f} s")
    console.print(f"Velocidad aproximada: {velocidad:.2f}x")
    console.print(f"Segmentos generados: {segmentos}")