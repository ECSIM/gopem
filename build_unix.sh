#!/bin/bash
py_version=$(python3 -V 2>&1 | grep -Po '(?<=Python )(.+)')
echo "Your Python Version : $py_version"
echo "Recommended Python Version : >= 3.6"
echo "-----"
echo "-----"
pip3 install "art==4.0"
pip3 install "requests==2.22.0"
pip3 install "matplotlib==3.1.1"
pip3 install "opem==1.4"
pip3 install "PyQt5==5.13.1"
pip3 install "setuptools>=40.9.0"
pip3 install "PyInstaller>=3.4"
if [[ "$OSTYPE" == "linux-gnu" ]]; then
        pyinstaller -y --clean --windowed GOPEM.spec
elif [[ "$OSTYPE" == "darwin"* ]]; then
    pyinstaller -y --clean --windowed GOPEM.spec
	pushd dist
	rm -r GOPEM
	mkdir GOPEM
	mv GOPEM-Portable GOPEM/
	hdiutil create ./GOPEM.dmg -srcfolder GOPEM -ov
	popd
elif [[ "$OSTYPE" == "cygwin" ]]; then
        echo "You are usign $OSTYPE, that means you are using windows OS, so please run build_exe.bat instead."
elif [[ "$OSTYPE" == "msys" ]]; then
        echo "You are usign $OSTYPE, that means you are using windows OS, so please run build_exe.bat instead."
else
        echo "$OSTYPE is not compatiable. please add an issue for gopem."
fi
