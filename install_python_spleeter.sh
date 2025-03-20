#!/bin/bash
URL_PYTHON_3_10_16="https://www.python.org/ftp/python/3.10.16/Python-3.10.16.tgz"
PYTHON_BIN="/usr/local/bin/python3.10"
PATH_PROJECT="$(pwd)"
PATH_ENV="$PATH_PROJECT/env_spleeter"
PATH_REQUIREMENTS="$PATH_PROJECT/requirements_spleeter.txt"

# Se instalan dependencias.
sudo pacman -Sy --needed base-devel gcc make zlib xz tk

# Cambiamos al path donde vamos a guardar todo e instalamos.
cd /usr/local/src
sudo curl -O $URL_PYTHON_3_10_16
sudo tar -xf Python-3.10.16.tgz
cd Python-3.10.16
sudo ./configure --enable-optimizations
sudo make -j$(nproc)
sudo make altinstall
# Revisamos la version.
/usr/local/bin/python3.10 --version

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
