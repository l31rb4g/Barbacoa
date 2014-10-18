#!/bin/bash

_python='C:/Python27/python.exe'
_pyinstaller='C:/PyInstaller-2.1/pyinstaller.py'
_build_path='BUILD'
_include_paths=(bbqlib plugins www)

echo '\n\n'
echo '+-----------------------------+'
echo '| Starting build for win32    |'
echo '+-----------------------------+'
echo '\n\n'


rm -rf $_build_path
mkdir $_build_path

trees=''
for p in ${_include_paths[@]}; do
    trees=$trees"Tree('../"$p"', prefix='"$p"'), "
done

$_python $_pyinstaller barbacoa.py \
    --onefile \
    --specpath="$_build_path" \
    --distpath="$_build_path/dist" \
    --workpath="$_build_path/build" \
    --hidden-import=uuid \
    --hidden-import=gzip
	
mv $_build_path/barbacoa.spec $_build_path/barbacoa-orig.spec
sed 's/exe = EXE(pyz,/exe = EXE(pyz, '$trees'/' $_build_path/barbacoa-orig.spec > $_build_path/barbacoa.spec

$_python $_pyinstaller barbacoa.py $_build_path/barbacoa.spec


echo '\n\n'
echo '+-----------------------------+'
echo '| Build finished!             |'
echo '+-----------------------------+'