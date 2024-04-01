@echo off
FOR /F "tokens=* USEBACKQ" %%F IN (`python --version`) DO (
SET py_version_str=%%F
)
SET py_version=%py_version_str:~7%

echo Your Python Version : %py_version%
echo Recommended Python Version : ^>= 3.6
echo -----
echo -----
python -m pip install "art==4.0"
python -m pip install "requests==2.22.0"
python -m pip install "matplotlib==3.1.1"
python -m pip install "opem==1.4"
python -m pip install "PyQt5==5.13.1"
python -m pip install "setuptools>=40.9.0"
python -m pip install "PyInstaller>=3.4"
python -m PyInstaller GOPEM.spec
pause