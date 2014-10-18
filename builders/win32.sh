#!/bin/bash

_python='C:/Python27/python.exe'
_pyinstaller='C:/PyInstaller-2.1/pyinstaller.py'
_build_path='BUILD'


rm -rf $_build_path
mkdir $_build_path


$_python $_pyinstaller ./barbacoa.py \
    --onefile \
    --windowed \
    --specpath="$_build_path" \
    --distpath="$_build_path/dist" \
    --workpath="$_build_path/build" \
    --hidden-import=uuid \
    --hidden-import=gzip \