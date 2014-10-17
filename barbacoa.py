#!/usr/bin/python
import os
import re
import json
import urllib
from PyQt4 import QtCore, QtGui, QtWebKit
from bbqlib.file import File
from bbqlib.environment import Environment


class Barbacoa():

    def __init__(self):
        self.CURRENT_PATH = os.path.dirname(__file__)
        self.PLUGIN_PATH = self.CURRENT_PATH + '/plugins'
        self.CONFIG = self.read_config(self.CURRENT_PATH + '/config.json')
        path = self.CURRENT_PATH + '/www/' + self.CONFIG['index']

        self.modules = {
            'Environment': Environment(self),
            'File': File(self)
        }

        self.app = QtGui.QApplication([])
        self.app.desktop().screen().rect().center()

        self.view = QtWebKit.QWebView()
        self.view.load(QtCore.QUrl(path))
        self.view.setFixedSize(self.CONFIG['dimensions']['width'], self.CONFIG['dimensions']['height'])
        self.view.setWindowTitle(self.CONFIG['title'])

        self.plugins = {}
        for plugin in self.CONFIG['plugins']:
            plugin = str(plugin)
            self.plugins[plugin] = __import__('plugins.' + plugin + '.' + plugin, globals(), locals(), '*', -1)

        self.view.connect(self.view, QtCore.SIGNAL("loadFinished(bool)"), self.ready)
        self.view.connect(self.view, QtCore.SIGNAL("urlChanged(QUrl)"), self.handle_request)

        self.view.adjustSize()
        self.view.move(self.app.desktop().screen().rect().center() - self.view.rect().center())

        self.view.show()
        self.app.exec_()

    def read_config(self, config_file):
        with open(config_file, 'r') as f:
            content = f.read()
        if content:
            content = json.loads(content)
            return content

        return False

    def send_callback(self, content):
        content = urllib.quote(content)
        self.execute('$_BBQ.execute_callback("' + content + '")')

    def ready(self):
        with open(self.CURRENT_PATH + '/bbqlib/barbacoa.js', 'r') as fjs:
            js = fjs.read()
        self.execute(js)

    def handle_request(self, request):
        request = str(request)
        regex = r'^.*#BBQ[1-2]::([^|]+)\|(.*)\'\)$'
        data = re.findall(regex, request)
        if data:
            action = data[0][0]
            params = json.loads(urllib.unquote(data[0][1]))

            if action == 'load-plugins':
                for plugin in self.CONFIG['plugins']:
                    with open(self.PLUGIN_PATH + '/' + plugin + '/' + plugin + '.js') as f:
                        js = f.read()
                        self.execute(js)

            #Environment module
            elif action == 'Environment.get_user_home':
                self.modules['Environment'].get_user_home(*params)

            #File module
            elif action == 'File.write':
                self.modules['Environment'].write(*params)
            elif action == 'File.choose_directory':
                self.modules['File'].choose_directory(*params)

    def execute(self, code):
        sender = QtWebKit.QWebView.sender(self.view)
        if re.findall('QWebPage', str(sender)):
            sender = sender.mainFrame()
        if sender:
            sender.evaluateJavaScript(code)


if __name__ == '__main__':
    Barbacoa()