import os


class Environment():

    def __init__(self, barbacoa):
        self.barbacoa = barbacoa

    def get_user_home(self):
        path = os.path.expanduser('~')
        path = path.replace('\\', '\\\\')
        self.barbacoa.send_callback(path)