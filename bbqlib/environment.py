import os
import urllib


class Environment():

    def __init__(self, barbacoa):
        self.barbacoa = barbacoa

    def get_user_home(self):
        path = os.path.expanduser('~')
        path = urllib.quote(path)
        self.barbacoa.send_callback(path)