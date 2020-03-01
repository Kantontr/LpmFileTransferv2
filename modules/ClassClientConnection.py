import os
import socket
import sys
import time


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

    def createConnection(self):
        # print ("file_path: {}".format(file_path))
        print ("Connection ip: {}".format(self.connection_ip))
        print ("Connection port: {}".format(self.connection_port))

        self.s = socket.socket()
        self.s.connect((self.connection_ip, int(self.connection_port)))

    def findFileNameFromPath(self, file_path):
        list = file_path.split("\\")
        filename = list[-1] #last element of the list
        return filename

    def sendFile(self, filepath, dirpath):
        filename = self.findFileNameFromPath(filepath)
        filesize = int(os.path.getsize(filepath))
        sendmode = "-File"
        messagetosend = str(sendmode + self.separator + str(
            filesize) + self.separator + filename + self.separator + dirpath + self.separator)
        msg = messagetosend.encode('utf-8')
        print("sending: {}".format(msg))
        self.s.send(msg)

        print ("==============================================")
        print ("Starting the transfer")
        print ("==============================================")
        time.sleep(2)

        filetosend = open(filepath, 'rb')
        line = filetosend.read(self.PACKET_SIZE)

        bytes_sent = 0
        while line:
            self.s.sendall(line)
            bytes_sent += self.PACKET_SIZE

            se_bytes = round(bytes_sent / 1000000, 2)
            se_file_size = round(filesize / 1000000, 2)
            se_perc = round(((bytes_sent / filesize) * 100), 2)
            print("\rProgress: {:.2f}/{} mb sent,{}%".format(se_bytes, se_file_size, se_perc), end="\r")

            line = filetosend.read(self.PACKET_SIZE)
        filetosend.close()
        # s.close()

        time.sleep(2)

    def endConnection(self):
        msg = "CloseSocket" + self.separator
        self.s.send(msg.encode('utf-8'))
        print ("Connection with {} closed".format(self.connection_ip))
        self.s.close()
