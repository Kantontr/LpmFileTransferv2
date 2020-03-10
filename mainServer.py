#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time

from modules import database
from modules import settings
from modules import ClassServerConnection


def main():
    Settings = settings.Settings()

    # db.LoadDatabaseFromFile()
    testServer = ClassServerConnection.ServerConnection("192.168.1.3", int("50001"))


if __name__ == '__main__':
    main()