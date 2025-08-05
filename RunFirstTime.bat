echo "Starte macOS-Python-Setup..."

echo "Python-Version:"
python3 --version

echo "Pip-Version:"
pip3 --version

echo "Aktualisiere pip..."
pip3 install --upgrade pip

pip3 install numpy

echo "Setup abgeschlossen!"

cd /d "%~dp0"


./RunProgram.bat