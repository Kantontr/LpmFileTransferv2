import os

class Database:

    def __init__(self):
        self.databasePath = "config\\database.lpm"
        self.separator = "<SEPARATOR>"

    databasePath = "config\\database.lpm"
    separator = "<SEPARATOR>"
    saved_user = {}  # saved user name, ip, port

    def checkIfUserExist(self, username):
        if username in self.saved_user:
            return True
        return False

    def checkIfIpExist(self, ip):
        for i, j in self.saved_user.items():
            if self.saved_user[i][0] == ip:
                return True
        return False

    def printDatabase(self):
        print("printDatabase:Printing")
        for i, j in self.saved_user.items():
            print(i, j)

    def AddUser(self, new_username, new_ip, new_port, new_comment):

        if len(new_username) < 0:
            return "Username is empty"
        if len(new_ip) < 0:
            return "ip is empty"
        if len(new_port) < 0:
            return "port is empty"
        if not self.checkIfUserExist(new_username):
            if not self.checkIfIpExist(new_ip):
                self.saved_user[new_username] = [new_ip, new_port, new_comment]
                if self.checkIfUserExist(new_username):
                    self.SaveDatabaseToFile()
                    return "User Added"
        return "Operation failed"

    def EditUser(self, old_username, new_username, new_ip, new_port, new_comment):

        if not self.checkIfUserExist(old_username):
            return "Error finding existing user"

        backup = [old_username, self.saved_user[old_username][0], self.saved_user[old_username][1],
                  self.saved_user[old_username][2]]  # creates backup in case new data is incorrect
        del self.saved_user[old_username]

        result = self.AddUser(new_username, new_ip, new_port, new_comment)

        if result == "User Added":
            self.SaveDatabaseToFile()
            return "Operation Successfull"
        else:
            result = self.AddUser(backup[0], backup[1], backup[2], backup[3])
            if result != "User Added":  # if backup cannot be loaded, load a backup from file
                print("Fatal error editing entry! Reloading backup from file")
                self.LoadDatabaseFromFile()
                return "Operation Failed. No changes"

    def LoadDatabaseFromFile(self):

        dbFile = open(self.databasePath, "r")

        self.saved_user.clear()
        while True:
            line = dbFile.readline()
            if len(line) > 0:
                list = line.split(self.separator)
                list[3] = list[3][0:len(list[3]) - 1]
                self.saved_user[list[0]] = [list[1], list[2], list[3]]
            else:
                break
        self.printDatabase()
        print("LoadDatabaseFromFile:Loaded")

    def SaveDatabaseToFile(self):

        dbFile = open(self.databasePath, "w")

        for i in self.saved_user:
            dbFile.write(i + self.separator)
            list = self.saved_user.get(i)
            dbFile.write(list[0] + self.separator + list[1] + self.separator + list[2] + "\n")
        dbFile.close()
        print("SaveDatabaseToFile:Saved")
