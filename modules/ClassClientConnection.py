import os
import socket
import sys
import time
import hashlib
from . import LPMRsaEncrypt


class ClientConnection:
    def __init__(self, name, ip, port):
        self.connection_name = name
        self.connection_ip = ip
        self.connection_port = port
        self.PACKET_SIZE = 2048
        self.separator = "<S3P4>"
        self.valTimeout = 20.0
        self.s = None
        self.connection_encrypted = "true"
        self.rsaCrypt = LPMRsaEncrypt.LPMRsaEncrypt(self.PACKET_SIZE)
        if self.createConnection():
            self.s.settimeout(self.valTimeout)
            if self.connection_encrypted == "true":
                try:
                    self.encryptConnection()
                except:
                    pass
            # if not self.checkConnection():
            #    self.endConnection()

    def __del__(self):
        print ("Deconstructor called. Ending connection with {}:{}".format(self.connection_ip, self.connection_port))


    def createConnection(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.connection_ip, int(self.connection_port)))
            print ("Connection with {}:{} initialized".format(self.connection_ip, self.connection_port))
            return True
        except:
            print ("Connection with {}:{}  could not be initialized".format(self.connection_ip, self.connection_port))
            return False

    def findFileNameFromPath(self, file_path):
        list = file_path.split("\\")
        return list[-1]  # last element of the list

    def encryptConnection(self):

        self.s.send(b'EncryptConnection')

        # waiting for server's public key
        serverPublicKey = self.s.recv(self.PACKET_SIZE)
        print ("Server public key received!")
        self.rsaCrypt.setEncryptor(serverPublicKey.decode())

        clientPublicKey = self.rsaCrypt.getPublicKey()
        # sending client's public key to Server
        self.s.send(clientPublicKey.encode())
        print ("Client public key sent.")

        # send encoded handshake
        msg = self.rsaCrypt.encryptLine("clienthandshake")
        self.s.send(msg)
        print ("Encrypted handshake sent to server")
        msgEnc = self.s.recv(self.PACKET_SIZE)
        msg = self.rsaCrypt.decryptLine(msgEnc)

        if msg == "Returning handshake":
            print ("Server returned handshake.\nConnection Established")
            return True
        else:
            return False

    def sendRawMessage(self, message):

        if self.connection_encrypted == "true":
            message = self.rsaCrypt.encryptLine(message)

        if isinstance(message, str):
            message = message.encode()

        self.s.send(message)

    def sendFile(self, filepath, dirpath):
        filename = self.findFileNameFromPath(filepath)
        filesize = int(os.path.getsize(filepath))
        messagetosend = str("-File" + self.separator + str(
            filesize) + self.separator + filename + self.separator + dirpath + self.separator)
        self.sendRawMessage(messagetosend)

        print ("===========================")
        print ("Initializing transfer")
        print ("===========================")

        if not self.waitForServer("ready"):
            print ("Server did not respond in time. Transfer aborted")
            return False
        else:
            print ("Starting the transfer")

        filetosend = open(filepath, 'rb')
        line = filetosend.read(self.PACKET_SIZE)
        bytes_sent = 0

        while line:
            # if self.connection_encrypted == "true":
            #     line = self.rsaCrypt.encryptLine(line)

            self.s.sendall(line)  # Send line
            bytes_sent += len(line)  # Add amount ob bytes sent to counter
            self.progressBar(bytes_sent, filesize)  # update progress bar
            line = filetosend.read(self.PACKET_SIZE)  # get new line from file
        filetosend.close()

        self.s.sendall(self.getmd5(filepath).encode())  # send md5 hash to server

        if self.waitForServer("Succes"):  # wait for server to confirm md5 hash
            return True
        else:
            print ("Error transfering file")
            return False

    def progressBar(self, bytesSent, baseSize):
        percentage = (bytesSent / baseSize) * 100
        percentage = round(percentage, 1)

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
        try:
            msg = self.s.recv(self.PACKET_SIZE)
            if self.connection_encrypted == "true":
                msg = self.rsaCrypt.decryptLine(msg)

            if not isinstance(msg, str):
                try:
                    msg = msg.decode()
                except:
                    pass

            print ("Got {} from server".format(msg))
            if msg == keyword:
                return True
        except:
            print ("Connection timeout with {}:{}".format(self.connection_ip, self.connection_port))

    def getmd5(self, filepath):
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        print ("\n"
               "Client md5 for {}: {}".format(filepath, hash_md5.hexdigest()))
        return hash_md5.hexdigest()

    def checkConnection(self):
        print ("Checking connection")
        try:
            time.sleep(1)
            self.s.send(str("ConnectionCheck" + self.separator).encode())
            if self.waitForServer("ConnectionEstablished"):
                print ("Connection with {} {} established".format(self.connection_ip, self.connection_port))
                return True

            else:
                print ("An error occured. Connection is not established")
                return False

        except:
            print ("An except error occured. Connection is not established")
            return False

    def endConnection(self):
        msg = "CloseSocket" + self.separator
        try:
            self.s.send(msg.encode('utf-8'))
            self.s.close()
            print ("Connection with {} closed".format(self.connection_ip))
        except:
            print ("Connection with {} already closed".format(self.connection_ip))
