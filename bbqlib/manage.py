#!/usr/bin/python
import os
import sys

bbqpath = '/home/l31rb4g/www/Barbacoa/bbqlib'
if bbqpath not in sys.path:
    sys.path.append(bbqpath)

from barbacoa import Barbacoa


if __name__ == '__main__':

    if len(sys.argv) > 1:

        if sys.argv[1] == 'run':
            project_root = os.path.abspath(os.path.dirname(__file__))
            Barbacoa(project_root)