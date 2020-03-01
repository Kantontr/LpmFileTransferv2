import os
import os.path
from os import path


class Settings:

    def __init__(self):
        if not path.isfile(self.settingsPath):  # create settings file if not existing
            self.loadDefaultSettings()
            self.saveSettingsToFile()
        else:
            self.loadSettingsFromFile()

    settingsPath = "config\\settings.lpm"
    separator = "="
    settings = {}

    def loadDefaultSettings(self):
        print("Load default settings")
        self.settings["colorScheme"] = "dark"
        self.settings["serverIp"] = "192.168.1.3"
        self.settings["serverPort"] = "50000"
        self.settings["clientAutostart"] = "false"
        self.settings["ServerAutostart"] = "true"

    def saveSettingsToFile(self):
        print("Saving settings to file")
        settingsFile = open(self.settingsPath, "w")

        for i in self.settings:
            settingsFile.write(i + self.separator + self.settings.get(i) + "\n")

        settingsFile.close()

    def loadSettingsFromFile(self):
        print("Loading settings from file")
        settingsFile = open(self.settingsPath, "r")

        while True:
            line = settingsFile.readline()
            if len(line) > 0:
                key, val = line.split(self.separator)
                self.settings[key] = val

            else:
                break
