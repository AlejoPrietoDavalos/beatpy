#!/bin/bash
URL_PYTHON_3_10_16="https://www.python.org/ftp/python/3.10.16/Python-3.10.16.tgz"

# ---------- Arch Linux ----------
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
# ---------- Arch Linux ----------
