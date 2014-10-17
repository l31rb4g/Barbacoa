import os
from PyQt4 import QtGui


class File():

    def __init__(self, barbacoa):
        self.barbacoa = barbacoa

    def read(self, filename):
        with open(filename, 'r') as f:
            content = f.read()
        self.barbacoa.send_callback(content)

    def write(self, filename, content):
        with open(filename, 'w') as f:
            f.write(content)

    def choose_directory(self, selected_dir):
        if not selected_dir:
            selected_dir = os.path.expanduser('~')
        path = QtGui.QFileDialog().getExistingDirectory(None, "Choose directory", selected_dir)
        self.barbacoa.send_callback(path)