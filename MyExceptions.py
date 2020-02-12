# Derived from: https://docs.python.org/3/tutorial/errors.html

class Error(Exception):
    pass

class FormatError(Error):

    def __init__(self, message):
        self.message = message
