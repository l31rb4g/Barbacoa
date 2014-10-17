#!/usr/bin/python
import os
import re
import json
import urllib
from PyQt4 import QtCore, QtGui, QtWebKit

from bbqlib.utils import read_config
from bbqlib.file import File
from bbqlib.environment import Environment


def domready(webview, frame):
    with open(CURRENT_PATH + '/bbqlib/barbacoa.js', 'r') as fjs:
        js = fjs.read()
    view.execute_script(js)


def handle_request(webview, frame, request, action, decision):
    regex = r'^.*#BBQ[1-2]::([^|]+)\|(.*)$'
    data = re.findall(regex, request.props.uri)
    if data:
        action = data[0][0]
        params = json.loads(urllib.unquote(data[0][1]))

        if action == 'Environment.get_user_home':
            environment.get_user_home(*params)

        elif action == 'File.write':
            File.write(*params)


if __name__ == '__main__':
    CURRENT_PATH = os.path.dirname(__file__)
    CONFIG = read_config(CURRENT_PATH + '/config.json')
    path = CURRENT_PATH + '/www/' + CONFIG['index']
    environment = Environment()

    app = QtGui.QApplication([])

    view = QtWebKit.QWebView()
    view.load(QtCore.QUrl('file://' + path))
    view.show()

    app.exec_()