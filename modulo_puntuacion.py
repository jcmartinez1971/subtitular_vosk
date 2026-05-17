"""
Restauración automática de puntuación.
"""

from deepmultilingualpunctuation import PunctuationModel
from rich.console import Console

console = Console()


class RestauradorPuntuacion:
    """
    Restaura puntuación y mayúsculas.
    """

    def __init__(self):

        console.print(
            "[cyan][INFO][/cyan] Cargando modelo de puntuación..."
        )

        self.modelo = PunctuationModel()

    def restaurar(self, texto: str) -> str:
        """
        Restaura puntuación del texto.
        """

        texto = texto.strip()

        if not texto:
            return ""

        resultado = self.modelo.restore_punctuation(
            texto
        )

        return resultado