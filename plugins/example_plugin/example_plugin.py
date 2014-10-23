import sys


class ExamplePlugin:

    def get_version(self):
        version = sys.version
        return version