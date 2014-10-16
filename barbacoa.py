#!/usr/bin/python

import os
import re
import json
import gtk
import webkit
import urllib
from bbqlib.utils import read_config
from bbqlib.actions import Actions
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
    CURRENT_PATH = os.path.abspath(os.path.curdir)
    CONFIG = read_config('config.json')
    path = CURRENT_PATH + '/www/' + CONFIG['index']

    view = webkit.WebView()
    view.open('file://' + path)

    actions = Actions(view)
    environment = Environment(view)

    sw = gtk.ScrolledWindow()
    sw.add(view)

    win = gtk.Window(gtk.WINDOW_TOPLEVEL)
    win.add(sw)
    win.show_all()
    win.set_title(CONFIG['title'])
    win.resize(CONFIG['dimensions']['width'], CONFIG['dimensions']['height'])
    win.set_position(gtk.WIN_POS_CENTER_ALWAYS)
    #win.set_resizable(False)

    view.connect('document-load-finished', domready)
    view.connect('navigation-policy-decision-requested', handle_request)

    gtk.main()