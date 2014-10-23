#!/usr/bin/python
import os
import sys

bbqpath = None

if bbqpath not in sys.path:
    sys.path.append(bbqpath)

from barbacoa import Barbacoa


if __name__ == '__main__':

    if len(sys.argv) > 1:

        if sys.argv[1] == 'run':
            project_root = os.path.abspath(os.path.dirname(__file__))
            Barbacoa(project_root)

        elif sys.argv[1] == 'build':

            if len(sys.argv) > 2:
                if sys.argv[2] == 'linux':
                    params = ''
                    print(os.popen('build.sh ' + params).read())

        else:
            print('Unknown command: ' + sys.argv[1])