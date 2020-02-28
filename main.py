#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time

from modules import database
from modules import settings

def main():

    Settings = settings.Settings()
    db = database.Database()
    print(db.AddUser("Knut","Ipknuta","PortKnuta","Knuteusz"))
    print(db.AddUser("Knut2", "Ipknuta2", "PortKnuta2",""))
    print(db.AddUser("Knut3", "Ipknuta3", "PortKnuta3",""))
    print(db.AddUser("Knut4", "Ipknuta4", "PortKnuta4",""))

    #print(db.EditUser("Knut3","Knut3", "Ipknuta5", "PortKnuta3","nowy com"))
    #print(db.EditUser("Knut4","Knut4", "Ipknuta4", "PortKnuta4", "knucica4",))
    db.LoadDatabaseFromFile()


if __name__ == '__main__':
    main()