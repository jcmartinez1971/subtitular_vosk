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


# SUBTITULAR_VOSK

Subtitulador offline profesional usando:

- VOSK
- FFmpeg
- Transformers NLP
- Restauración automática de puntuación

Genera subtítulos `.srt` localmente sin conexión a internet
después de descargar los modelos necesarios.

---

````markdown id="8v2m5q"
# SUBTITULAR_VOSK

Subtitulador offline profesional usando:

- VOSK
- FFmpeg
- Transformers NLP
- Restauración automática de puntuación

Genera subtítulos `.srt` localmente sin conexión a internet
después de descargar los modelos necesarios.

---

# Requisitos

- Python 3.11
- FFmpeg

---

# ¿Por qué Python 3.11?

Este proyecto utiliza librerías NLP modernas como:

- transformers
- torch
- tokenizers
- deepmultilingualpunctuation

Actualmente Python 3.11 ofrece la mejor compatibilidad y
estabilidad para este ecosistema.

Versiones más recientes como Python 3.13 todavía presentan
problemas frecuentes con:

- wheels precompilados
- tokenizers
- compilación Rust
- dependencias de Transformers
- compatibilidad Torch/NLP

Usar Python 3.11 evita:

- errores de compilación
- instalación manual de Rust
- conflictos de dependencias
- fallos de instalación de tokenizers

y permite una instalación mucho más estable y reproducible.

---

# Crear entorno virtual

```powershell
py -3.11 -m venv venv
````

---

# Activar entorno virtual

```powershell
.\venv\Scripts\Activate.ps1
```

---

# Instalar dependencias

```powershell
pip install -r requirements.txt
```

---

# Modelos VOSK

Descargar modelos desde:

[https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)

Ejemplo recomendado:

```text
vosk-model-small-es-0.42
```

Colocar dentro de:

```text
modelos/
```

---

# Ejecución

```powershell
python subtitulador.py video.mp4 --modelo modelos\vosk-model-small-es-0.42
```

---

# Pipeline actual

```text
video/audio
↓
FFmpeg
↓
WAV PCM mono 16 kHz
↓
VOSK ASR
↓
texto + timestamps
↓
restauración NLP de puntuación
↓
segmentación SRT
↓
subtítulos finales
```

---

# Estado del proyecto

Actualmente el proyecto incluye:

* Transcripción offline
* Generación SRT
* Arquitectura modular
* Restauración automática de puntuación
* Pipeline NLP compatible con Transformers
* Compatibilidad Windows/Linux
* Procesamiento eficiente CPU
* Soporte para archivos largos
* Entorno reproducible

---

# Tecnologías utilizadas

* Python 3.11
* VOSK
* Kaldi
* FFmpeg
* Transformers
* Torch
* deepmultilingualpunctuation
* tqdm
* rich

```
```
