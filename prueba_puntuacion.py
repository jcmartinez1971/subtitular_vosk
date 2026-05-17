"""
Prueba de restauración de puntuación.
"""

from modulo_puntuacion import (
    RestauradorPuntuacion
)

texto = """
hello everyone today we will talk about
oauth authentication and access tokens
"""

restaurador = RestauradorPuntuacion()

resultado = restaurador.restaurar(
    texto
)

print("\nRESULTADO:\n")

print(resultado)