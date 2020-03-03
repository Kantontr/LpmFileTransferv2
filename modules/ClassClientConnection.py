import os
import socket
import sys
import time
import hashlib


class ClientConnection:
    def __init__(self, name, ip, port):
        self.connection_name = name
        self.connection_ip = ip
        self.connection_port = port
        self.createConnection()

    PACKET_SIZE = 1024
    separator = "<SEPARATOR>"
    connection_name = None
    connection_ip = None
    connection_port = None
    s = None
    valTimeout = 5

    def createConnection(self):
        # print ("file_path: {}".format(file_path))
        print ("Connection ip: {}".format(self.connection_ip))
        print ("Connection port: {}".format(self.connection_port))

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.connection_ip, int(self.connection_port)))

    def findFileNameFromPath(self, file_path):
        list = file_path.split("\\")
        filename = list[-1]  # last element of the list
        return filename

    def sendFile(self, filepath, dirpath):
        filename = self.findFileNameFromPath(filepath)
        filesize = int(os.path.getsize(filepath))
        sendmode = "-File"
        messagetosend = str(sendmode + self.separator + str(
            filesize) + self.separator + filename + self.separator + dirpath + self.separator)
        msg = messagetosend.encode('utf-8')
        # print("sending: {}".format(msg))
        self.s.send(msg)

        print ("==============================================")
        print ("Starting the transfer")
        print ("==============================================")

        if not self.waitForServer("ready"):
            print ("Serer did not respond in time. Transfer aborted")
            return False
        else:
            print ("transfer begins")

        filetosend = open(filepath, 'rb')
        line = filetosend.read(self.PACKET_SIZE)

        bytes_sent = 0
        while line:
            self.s.sendall(line)
            bytes_sent += len(line)
            self.progressBar(bytes_sent, filesize)
            line = filetosend.read(self.PACKET_SIZE)
        filetosend.close()

        self.s.sendall(self.getmd5(filepath).encode())

        if self.waitForServer("Succes"):
            return True
        else:
            print ("Error transfering file")
            return False

    def progressBar(self, bytesSent, baseSize):
        percentage = (bytesSent / baseSize) * 100
        percentage = round(percentage, 1)
        # print ("{}% Done".format(percentage), end="\r")

        if baseSize < 1000000:  # smaller than 1mb
            divid = 1000
            unit = "kB"
        elif baseSize < 1000000000:  # smaller than 1gb
            divid = 1000000
            unit = "mB"
        else:
            divid = 1000000000
            unit = "gB"

        if percentage.is_integer():
            val1 = round(bytesSent / divid, 2)
            val2 = round(baseSize / divid, 2)
            print("\rProgress: {}/{} {} sent,{}%".format(val1, val2, unit, percentage), end="\r")

    def waitForServer(self, keyword):

        timeout = 0
        while timeout < self.valTimeout:
            msg = self.s.recv(self.PACKET_SIZE)
            if len(msg) != 0:
                print (msg.decode())
                if msg.decode() == keyword:
                    return True
            time.sleep(1)
            timeout += 1

        print ("Connection timeout!")
        return False

    def getmd5(self, filepath):
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        print ("\n"
               "Client md5 for {}: {}".format(filepath, hash_md5.hexdigest()))
        return hash_md5.hexdigest()

    def endConnection(self):
        msg = "CloseSocket" + self.separator
        self.s.send(msg.encode('utf-8'))
        print ("Connection with {} closed".format(self.connection_ip))
        self.s.close()
