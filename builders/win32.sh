#!/bin/bash

_python='C:/Python27/python.exe'
_pyinstaller='C:/PyInstaller-2.1/pyinstaller.py'
_build_path='BUILD'
_include_paths=(bbqlib plugins www)

echo -e '\n\n'
echo '+-----------------------------+'
echo '| Starting build for win32    |'
echo '+-----------------------------+'
echo -e '\n\n'


rm -rf $_build_path
mkdir $_build_path

trees=''
for p in ${_include_paths[@]}; do
    trees=$trees"Tree('"$p"', prefix='"$p"'), "
done
trees=$(echo $trees | sed "s/\//\\\\\//g")

$_python $_pyinstaller barbacoa.py \
    --onefile \
    --specpath="$_build_path" \
    --distpath="$_build_path/dist" \
    --workpath="$_build_path/build" \
    --hidden-import=plugins.groovesync.groovesync \
    --hidden-import=uuid \
    --hidden-import=gzip
	
exp='s/exe = EXE(pyz,/exe = EXE(pyz, '$trees'/'
sed -i "$exp" $_build_path/barbacoa.spec

$_python $_pyinstaller $_build_path/barbacoa.spec \
    --specpath="$_build_path" \
    --distpath="$_build_path/dist" \
    --workpath="$_build_path/build"


echo -e '\n\n'
echo '+-----------------------------+'
echo '| Build finished!             |'
echo '+-----------------------------+'
echo -e '\n\n'

$_build_path/dist/barbacoa.exe