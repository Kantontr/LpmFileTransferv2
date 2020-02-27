import os


# d = {"Baltimore Ravens": [13, 3]}
# d["Baltimore Ravens"][0] += 1
# print d
# {"Baltimore Ravens": [14, 3]}

class database:
    saved_user = {}  # saved user name, ip, port

    def checkIfUserExist(self, username):
        if username in self.saved_user:
            print("Username exist")
            return True
        return False

    def checkIfIpExist(self, ip):
        for i, j in self.saved_user.items():
            if self.saved_user[i][0] == ip:
                print("IP exist")
                return True
        return False

    def printDatabase(self):
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
                    return "Operation Succesfull"
        return "Operation failed"

    def EditUser(self, old_username, new_username, new_ip, new_port, new_comment):

        if not self.checkIfUserExist(old_username):
            return "Error finding existing user"

        backup = [old_username, self.saved_user[old_username][0], self.saved_user[old_username][1],
                  self.saved_user[old_username][2]]  # creates backup in case new data is incorrect
        del self.saved_user[old_username]

        result = self.AddUser(new_username, new_ip, new_port, new_comment)

        if result == "Operation Succesfull":
            self.SaveDatabaseToFile()
            return "Operation Successfull"
        else:
            result = self.AddUser(backup[0], backup[1], backup[2], backup[3])
            if result != "Operation Succesfull": #if backup cannot be loaded, load a backup from file
                print("Fatal error editing entry! Reloading backup from file")
                self.LoadDatabaseFromFile()
                return "Operation Failed. No changes"

    def LoadDatabaseFromFile(self):
        print("Load:Test")

    def SaveDatabaseToFile(self):
        print("Save:Test")
