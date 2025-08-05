echo "Start macOS-Python-Setup..."

echo "Python-Version:"
python3 --version

echo "Pip-Version:"
pip3 --version

echo "Update pip..."
pip3 install --upgrade pip

pip3 install numpy

echo "Setup Done!"

cd /d "%~dp0"


./RunProgram.bat