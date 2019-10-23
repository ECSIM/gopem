@echo off
FOR /F "tokens=* USEBACKQ" %%F IN (`python --version`) DO (
SET py_version_str=%%F
)
SET /A py_version=%py_version_str:~9,-2%
echo -----
if %py_version% LSS 5 (
	echo Warning : Please use Python ^> 3.5
) else (
	echo Python version check done!
)
echo -----
python -m PyInstaller GOPEM.spec
pause