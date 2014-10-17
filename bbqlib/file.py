class File():

    def __init__(self, barbacoa):
        self.barbacoa = barbacoa

    @staticmethod
    def write(filename, content):
        with open(filename, 'w') as f:
            f.write(content)