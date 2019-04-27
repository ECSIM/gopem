@echo off
python --version | find /i "Python 3.5" > nul
echo -----
if errorlevel 1 (
	echo Warning : Please use Python 3.5.x
) else (
	echo Python version check done!
)
echo -----
python -m PyInstaller GOPEM.spec
pause