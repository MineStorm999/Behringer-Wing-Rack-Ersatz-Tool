#!/bin/bash

echo "Start macOS-Python-Setup..."

# Prüfe Python-Version
echo "Python-Version:"
python3 --version

# Prüfe Pip-Version
echo "Pip-Version:"
pip3 --version

# Upgrade pip
echo "Update pip..."
pip3 install --upgrade pip

pip3 install numpy

# Tkinter-Verfügbarkeit prüfen
echo "Check Tkinter..."
python3 -c "import tkinter; print('Tkinter is available. Version:', tkinter.TkVersion)" \
  || {
    echo "Tkinter not found. Install via Homebrew..."
    if ! command -v brew &> /dev/null; then
      echo "Homebrew wird installiert..."
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    brew install python-tk
  }

echo "Setup Done!"

cd "$(dirname "${BASH_SOURCE[0]}")"


./RunProgram.command