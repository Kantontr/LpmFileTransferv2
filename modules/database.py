import os


class Database:

    def __init__(self):
        self.databasePath = "config\\database.lpm"
        self.saved_user = {}  # saved user name, ip, port
        self.databasePath = "config\\database.lpm"
        self.separator = "<SEPARATOR>"
        self.loadDatabaseFromFile()
        self.printDatabase()

    def checkIfUserExist(self, username):
        for i, j in self.saved_user.items():
            if self.saved_user[i][0] == username:
                return True
        return False

    def checkIfIpExist(self, ip):
        for i, j in self.saved_user.items():
            if self.saved_user[i][1] == ip:
                return True
        return False

    def printDatabase(self):
        print("printDatabase:Printing")
        for i, j in self.saved_user.items():
            print("id:{} Data: {}".format(i, j))

    def genNewId(self):
        i = 0
        while True:
            if str(i) not in self.saved_user:
                print ("New unique id: {}".format(i))
                return i
            i += 1


    def getId(self, username):
        for i, j in self.saved_user.items():
            if self.saved_user[i][0] == username:
                return i
        return False

    def addUser(self, new_username, new_ip, new_port, new_comment):

        if len(new_username) < 0:
            return "Username is empty"
        if len(new_ip) < 0:
            return "ip is empty"
        if len(new_port) < 0:
            return "port is empty"
        if not self.checkIfUserExist(new_username):
            if not self.checkIfIpExist(new_ip):
                uniqueId = self.genNewId()
                self.saved_user[uniqueId] = [new_username, new_ip, new_port, new_comment]
                if self.checkIfUserExist(new_username):
                    self.saveDatabaseToFile()
                    return "User Added"
        return "Operation failed"

    def editUser(self, old_username, new_username, new_ip, new_port, new_comment):

        if not self.checkIfUserExist(old_username):
            return "Error finding existing user"

        backup = [old_username, self.saved_user[old_username][0], self.saved_user[old_username][1],
                  self.saved_user[old_username][2]]  # creates backup in case new data is incorrect
        del self.saved_user[old_username]

        result = self.addUser(new_username, new_ip, new_port, new_comment)

        if result == "User Added":
            self.saveDatabaseToFile()
            return "Operation Successfull"
        else:
            result = self.addUser(backup[0], backup[1], backup[2], backup[3])
            if result != "User Added":  # if backup cannot be loaded, load a backup from file
                print("Fatal error editing entry! Reloading backup from file")
                self.loadDatabaseFromFile()
                return "Operation Failed. No changes"


    def removeUser(self,username):
        if self.checkIfUserExist(username):
            del self.saved_user[self.getId(username)]
            self.saveDatabaseToFile()

    def loadDatabaseFromFile(self):

        dbFile = open(self.databasePath, "r")

        self.saved_user.clear()
        while True:
            line = dbFile.readline()
            if len(line) > 0:
                list = line.split(self.separator)
                list[4] = list[4][0:len(list[4])-1]
                self.saved_user[list[0]] = [list[1], list[2], list[3], list[4]]
            else:
                break
        print("loadDatabaseFromFile:Loaded")

    def saveDatabaseToFile(self):

        dbFile = open(self.databasePath, "w")

        for i in self.saved_user:
            dbFile.write(str(i) + self.separator)
            list = self.saved_user.get(i)
            dbFile.write(
                list[0] + self.separator + list[1] + self.separator + list[2] + self.separator + list[3]+"\n")

        dbFile.close()
        print("saveDatabaseToFile:Saved")
