#!/bin/bash

_python='C:/Python27/python.exe'
_pyinstaller='C:/PyInstaller-2.1/pyinstaller.py'


$_python $_pyinstaller ./barbacoa.py -F --hidden-import=uuid --hidden-import=gzip