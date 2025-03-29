#!/bin/bash
PYTHON_BIN="/usr/local/bin/python3.10"
PATH_PROJECT="$(pwd)"
PATH_ENV="$PATH_PROJECT/_env_spleeter"
PATH_REQUIREMENTS="$PATH_PROJECT/requirements_spleeter.txt"

# Vuelve al path del projecto.
cd $PATH_PROJECT

if [ ! -d "$PATH_ENV" ]; then
    # Se crea el entorno, si no existiera.
    $PYTHON_BIN -m venv "$PATH_ENV"
fi

# Instalamos las dependencias si hiciera falta.
source "$PATH_ENV/bin/activate"
if [ -f "$PATH_REQUIREMENTS" ]; then
    pip install -r "$PATH_REQUIREMENTS"
fi
