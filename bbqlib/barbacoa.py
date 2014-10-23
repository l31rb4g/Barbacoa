#!/usr/bin/python
import os
import re
import sys
import json
import urllib
from PyQt4 import QtCore, QtGui, QtWebKit
from api.file import File
from api.environment import Environment


class Barbacoa():

    version = '0.2.0'

    def __init__(self, project_root):
        self.project_root = project_root
        self.CONFIG = {}
        execfile(project_root + '/config.py')

        if '--version' in sys.argv:
            print(self.version)
            return

        path = self.get_file(project_root + '/www/' + self.CONFIG['index'])

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
            if plugin:
                #self.plugins[plugin] = __import__('plugins.' + plugin + '.' + plugin, globals(), locals(), '*', -1)
                execfile(self.project_root + '/plugins/' + plugin + '/' + plugin + '.py', globals(), locals())

        self.view.connect(self.view, QtCore.SIGNAL("loadFinished(bool)"), self.ready)
        self.view.connect(self.view, QtCore.SIGNAL("urlChanged(QUrl)"), self.handle_request)

        self.view.adjustSize()
        self.view.move(self.app.desktop().screen().rect().center() - self.view.rect().center())

        self.view.show()
        self.app.exec_()

    def send_callback(self, content):
        content = urllib.quote(content)
        self.execute('$_BBQ.execute_callback("' + content + '")')

    def respond(self, response):
        if type(response) is bool:
            response = str(response).lower()
        else:
            response = '"' + urllib.quote(str(response)) + '"'

        self.execute('$_BBQ.response = ' + response)

    def ready(self):
        with open(self.get_file('barbacoa.js'), 'r') as fjs:
            js = fjs.read()
        self.execute(js)

    def handle_request(self, request):
        self.execute('$BBQ.response = true')
        request = str(request)
        regex = r'^.*#BBQ[1-2]::([^|]+)\|(.*)\'\)$'
        data = re.findall(regex, request)
        if data:
            action = data[0][0]
            params = json.loads(urllib.unquote(data[0][1]))

            if action == 'load-plugins':
                for plugin in self.CONFIG['plugins']:
                    if plugin:
                        plugin_path = self.get_file('plugins/' + plugin + '/' + plugin + '.js')
                        with open(plugin_path) as f:
                            js = f.read()
                        self.execute('$_BBQ.plugin_being_registred = "' + plugin + '"')
                        self.execute(js)

            elif action == 'execute-plugin':
                klass = getattr(self.plugins[params[0]], params[1])
                instance = klass()
                method = getattr(instance, params[2])
                r = method(*params[3])
                self.respond(r)

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

    def get_file(self, filename):
        if hasattr(sys, '_MEIPASS'):
            os.chdir(sys._MEIPASS)
            filename = sys._MEIPASS + '/' + filename
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)


if __name__ == '__main__':
    Barbacoa()