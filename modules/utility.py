import os
import os.path
from os import path

from modules import database
from modules import settings
from modules import ClassClientConnection
from modules import ClassServerConnection
from modules import LPMRsaEncrypt
from modules import stylesheet
from PyQt5 import QtCore, QtGui, QtWidgets


class Utility:

    def __init__(self):
        pass
        # self.settings = settings.Settings()
        # self.db = database.Database()

    def checkIfDirExist(self, path):
        if path.isdir(path):
            print("{} is a directory".format(path))
            return True
        else:
            print("{} is not a directory".format(path))
            return False

    def checkIfFileExist(self, path):
        if path.isfile(path):
            print("{} is a file".format(path))
            return True
        else:
            print("{} is not a file".format(path))
            return False


db = database.Database()
settings = settings.Settings()
stylesheet = stylesheet.Stylesheet()
stylesheet.setStyle(settings.settings["colorScheme"])
