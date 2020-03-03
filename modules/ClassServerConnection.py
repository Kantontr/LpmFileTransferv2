import socket  # Import socket module
import os
import time
import sys
import hashlib


class ServerConnection:

    def __init__(self, ip, port, SaveFilePath):
        self.connection_ip = ip  # localhost?
        self.connection_port = port
        self.defaultSaveFilePath = SaveFilePath
        self.createConnection()
        self.waitForConnection()

    PACKET_SIZE = 1024
    separator = "<SEPARATOR>"

    def createConnection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
        print ("Starting server on {} {}".format(self.connection_ip, self.connection_port))
        self.s.bind((self.connection_ip, self.connection_port))  # Bind to the port

    def waitForConnection(self):
        try:
            while True:
                self.s.listen(10)  # Now wait for client connection.
                print ('Server listening....')
                self.sock, self.addr = self.s.accept()
                print("User connected at: {}".format(self.addr))
                self.handleIncomingMessage()
        except:
            self.endConnection()

    def handleIncomingMessage(self):
        while True:
            received = self.sock.recv(1024)
            if not received:
                time.sleep(0.2)
                continue
            message = str(received)

            receivedMessage = message.split(self.separator)
            mode = receivedMessage[0][2:]  # delete "b from message

            if mode == "-File":
                self.receiveFile(int(receivedMessage[1]), receivedMessage[2], receivedMessage[3])
            elif mode == "CloseSocket":
                self.endConnection()
                return

            print ('Server listening....')

    def receiveFile(self, filesize, filename, dirpath):
        print("Receiving file!Size: {}, Name: {}, Dir: {}".format(filesize, filename, dirpath))

        bytes_received = 0
        save_file_path = self.defaultSaveFilePath + dirpath + "\\" + filename

        self.sendMessage("ready")
        with open(save_file_path, 'wb') as f:
            print('File opened. Beginning to save\n')
            while True:

                data = self.sock.recv(1024)
                if not data:
                    break
                f.write(data)
                bytes_received += len(data)

                self.progressBar(bytes_received, filesize)
                if bytes_received >= filesize:
                    f.close()
                    if self.checkFileIntegrity(save_file_path):
                        self.sendMessage("Succes")
                        print('Successfully got the file\n')
                        return True
                    else:
                        self.sendMessage("Fail")
                        print('Error getting the file\n')
        f.close()
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

    def checkFileIntegrity(self, filename):
        md5Server = self.getmd5(filename)

        timeout = 0
        while timeout < 5:
            data = self.sock.recv(1024)
            if data:
                md5Client = data.decode()
                if data:
                    print ("Expecting {} got {}".format(md5Server,md5Client))
                if md5Client == md5Server:
                    print ("MD5 match")
                    return True
                else:
                    print ("MD5 no match")
                    return False
            else:
                timeout += 1
                time.sleep(1)
        print ("Connection timed out")  # if failed to get md5 from server for 10sec

    def sendMessage(self, message):
        print("Sending {} to {}".format(message, self.addr))
        self.sock.sendall(message.encode())

    def getmd5(self, filepath):
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        print ("\n"
               "Server md5 for {}: {}".format(filepath, hash_md5.hexdigest()))
        return hash_md5.hexdigest()

    def endConnection(self):
        print("Connection with {} closed".format(self.addr))
        self.s.close()
        self.createConnection()
        self.waitForConnection()
