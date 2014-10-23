#!/usr/bin/python
import sys
import os
import shutil


class BarbacoaAdmin():

    def __init__(self):
        self.barbacoa_root = os.path.dirname(__file__)
        self.project_root = os.path.abspath(os.path.curdir)

    def start_project(self, name):
        if name:
            new_root = self.project_root + '/' + name
            os.mkdir(new_root)
            self.project_root = new_root
            shutil.copytree(self.barbacoa_root + '/plugins', self.project_root + '/plugins')
            shutil.copytree(self.barbacoa_root + '/www', self.project_root + '/www')
            shutil.copyfile(self.barbacoa_root + '/bbqlib/manage.py', self.project_root + '/manage.py')
            os.chmod(self.project_root + '/manage.py', 0755)
            shutil.copyfile(self.barbacoa_root + '/bbqlib/config.py', self.project_root + '/config.py')
            print('[Barbacoa] New Barbacoa project started on ' + self.project_root)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        bbq = BarbacoaAdmin()

        if sys.argv[1] == 'startproject':
            name = sys.argv[2] if len(sys.argv) > 2 else None
            while not name:
                print('Type the name for the new Barbacoa project:'),
                name = raw_input()

            bbq.start_project(name)