@echo off
FOR /F "tokens=* USEBACKQ" %%F IN (`python --version`) DO (
SET py_version_str=%%F
)
SET py_version=%py_version_str:~7%

echo Your Python Version : %py_version%
echo Recommended Python Version : ^>= 3.5
echo -----
echo -----
python -m pip install -r requirements.txt
python setup.py install
python -m pip install "PyInstaller>=3.3"
python -m PyInstaller GOPEM.spec
pause