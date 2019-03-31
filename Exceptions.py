class IllegalFileSystemOperation(Exception):
    def __init__(self, message):
        Exception.__init__(self, "Illegal File Operation: {0}".format(message))
        self.type = "Illegal File Operation"
        self.message = message


class PathNotFound(Exception):
    def __init__(self, message):
        Exception.__init__(self, "Path Not Found: {0}".format(message))
        self.type = "Path Not Found"
        self.message = message


class PathAlreadyExists(Exception):
    def __init__(self, message):
        Exception.__init__(self, "Path Already Exists: {0}".format(message))
        self.type = "Path Already Exists"
        self.message = message


class NotATextFile(Exception):
    def __init__(self, message):
        Exception.__init__(self, "Not A Text File: {0}".format(message))
        self.type = "Not A Text File"
        self.message = message
