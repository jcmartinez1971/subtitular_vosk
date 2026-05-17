@echo off
REM =========================================================
REM Creador de estructura profesional para subtitular_vosk
REM =========================================================

echo.
echo ==========================================
echo   CREANDO ESTRUCTURA DEL PROYECTO VOSK
echo ==========================================
echo.

REM Crear carpetas principales
mkdir modelos
mkdir logs
mkdir temp

REM Crear ambiente virtual
echo [INFO] Creando ambiente virtual...
python -m venv venv

REM Crear archivos principales
echo [INFO] Creando archivos Python...

type nul > subtitulador.py
type nul > transcriptor.py
type nul > generador_srt.py
type nul > audio_utils.py
type nul > utilidades.py
type nul > diagnostico_transcripcion.py

REM Crear archivos auxiliares
type nul > requirements.txt
type nul > README.md
type nul > .gitignore

REM Escribir requirements.txt
echo vosk> requirements.txt
echo rich>> requirements.txt
echo tqdm>> requirements.txt

REM Escribir .gitignore
echo venv/> .gitignore
echo __pycache__//>> .gitignore
echo temp/>> .gitignore
echo logs/>> .gitignore
echo *.wav>> .gitignore

echo.
echo ==========================================
echo   ESTRUCTURA CREADA CORRECTAMENTE
echo ==========================================
echo.

echo [INFO] Para activar el ambiente virtual:
echo.
echo     .\venv\Scripts\Activate.ps1
echo.
echo [INFO] Luego instalar dependencias:
echo.
echo     pip install -r requirements.txt
echo.

pause