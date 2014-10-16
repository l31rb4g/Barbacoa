class File():

    def __init__(self, view):
        self.view = view

    @staticmethod
    def write(filename, content):
        with open(filename, 'w') as f:
            f.write(content)