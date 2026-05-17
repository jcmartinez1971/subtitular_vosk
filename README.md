# SUBTITULAR_VOSK

Subtitulador offline usando VOSK + FFmpeg.

## Requisitos

- Python 3.10+
- FFmpeg

## Instalación

python -m venv venv

Activar entorno:

.\venv\Scripts\Activate.ps1

Instalar dependencias:

pip install -r requirements.txt

## Modelos

Descargar modelos VOSK:

https://alphacephei.com/vosk/models

Colocar en:

modelos/

## Ejecución

python subtitulador.py video.mp4 --modelo modelos/vosk-model-small-es-0.42