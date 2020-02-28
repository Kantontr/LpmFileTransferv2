import os
import os.path
from os import path

class Utility:

    def __init__(self):
        None

    def checkIfDirExist(self,path):
        if path.isdir(path):
            print("{} is a directory".format(path))
            return True
        else:
            print("{} is not a directory".format(path))
            return False

    def checkIfFileExist(self,path):
        if path.isfile(path):
            print("{} is a file".format(path))
            return True
        else:
            print("{} is not a file".format(path))
            return False