import os


class Environment():

    def __init__(self, barbacoa):
        self.barbacoa = barbacoa

    def get_user_home(self):
        self.barbacoa.send_callback(os.path.expanduser('~'))