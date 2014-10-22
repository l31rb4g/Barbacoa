#!/bin/bash

_include_paths=(bbqlib plugins www)

if [ "$1" == --'windows' ]; then
    is_windows=1
fi

if [ $is_windows ]; then
    _python='C:/Python27/python.exe'
    _pyinstaller='C:/PyInstaller-2.1/pyinstaller.py'
    _build_path='BUILD/win32'
else
    _python=''
    _pyinstaller='pyinstaller.py'
    _build_path='BUILD/linux'
fi

echo -e '\n\n'
echo '=========================='
echo ' Starting build'
echo '=========================='
echo -e '\n\n'


rm -rf $_build_path
mkdir -p $_build_path

trees=''
for p in ${_include_paths[@]}; do
    trees=$trees"Tree('"$p"', prefix='"$p"'), "
done
trees=$(echo $trees | sed "s/\//\\\\\//g")

exp='s/exe = EXE(pyz,/exe = EXE(pyz, '$trees'/'
sed -i "$exp" $_build_path/barbacoa.spec

$_python $_pyinstaller barbacoa.spec \
    --specpath="$_build_path" \
    --distpath="$_build_path/dist" \
    --workpath="$_build_path/build"


echo -e '\n\n'
echo '+-----------------------------+'
echo '| Build finished!             |'
echo '+-----------------------------+'
echo -e '\n\n'