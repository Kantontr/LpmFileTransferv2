import socket  # Import socket module
import os
import time
import sys
import hashlib
import threading
from . import LPMRsaEncrypt, ClassClientConnection, ClassServerConnection, progressbar
from modules import utility, settings
import queue


class Connection:

    def __init__(self, connectionSide, ip, port):
        self.connectionSide = connectionSide  # server or client
        self.client = False
        self.Server = False

        if self.connectionSide == "server":
            self.server = True
        elif self.connectionSide == "client":
            self.client = True

        self.status = "online"
        self.connection_ip = ip
        self.connection_port = port
        self.socket = None

        self.OutputQueue = queue.Queue()
        self.InternalQueue = queue.Queue()

        self.socketBusy = threading.Event()

        self.serverThread = threading.Thread(target=self.serverThread)


        if self.connectionSide == "server":
            self.connection = ClassServerConnection.ServerConnection(self.connection_ip, self.connection_port)
            self.socket = self.connection.sock
            self.serverThread.start()
            self.status = "Connected"
        elif self.connectionSide == "client":
            self.connection = ClassClientConnection.ClientConnection("test", self.connection_ip, self.connection_port)
            self.socket = self.connection.s
            self.serverThread.start()
            self.status = "Connected"


    def sendMessage(self, message):
        msg = ("-Message" + self.connection.separator + message)
        if self.connection.connection_encrypted == "true":
            msg = self.connection.rsaCrypt.encryptLine(msg)
        else:
            msg = message.encode()
        self.socket.sendall(msg)

    def serverThread(self):
        print ("Starting server thread with id: {}".format(threading.current_thread().ident))
        self.status = "Connected"
        while True:
            print ('Server listening...')
            self.waitForMessage()

    def waitForMessage(self):

        print ("\nWaiting for new message\n")
        received = self.socket.recv(self.connection.PACKET_SIZE)

        if self.connection.connection_encrypted == "true":
            message = self.connection.rsaCrypt.decryptLine(received)
        else:
            message = str(received.decode())

        receivedMessage = message.split(self.connection.separator)
        mode = receivedMessage[0]  # get mode from message
        print ("Mode: {}".format(mode))

        if mode == "-File":
            self.receiveFile(int(receivedMessage[1]), receivedMessage[2], receivedMessage[3])

        elif mode == "-Message":
            print ("Got message: {}".format(receivedMessage[1]))
            self.OutputQueue.put(receivedMessage[1])

        elif mode == "EncryptConnection":
            print ("Encrypting connection")
            self.status = "Encrypting connection..."
            self.connection.encryptConnection()

        elif mode == "CloseSocket":
            self.status = "Disconecting"
            self.connection.endConnection()
            self.status = "Disconnected"
            return

        elif mode == "-Internal":
           if receivedMessage[1] == "-transfer":
               self.TransferQueue.put(receivedMessage[2])

    def sendFile(self, filepath, subDir):

        # create new queue for this file operation

        self.TransferQueue = queue.Queue()
        self.status = "Sending File(s)"

        filename = self.findFileNameFromPath(filepath)
        filesize = int(os.path.getsize(filepath))
        messagetosend = str("-File" + self.connection.separator + str(
            filesize) + self.connection.separator + filename + self.connection.separator + subDir + self.connection.separator)
        self.sendRawMessage(messagetosend)

        print ("Initializing transfer. Requesting accept")

        if not self.waitForServer("accept"):
            print ("Server did not respond in time. Transfer aborted")
            return False
        else:
            print ("File transfer accepted by server. Starting the transfer")
        filetosend = open(filepath, 'rb')
        line = filetosend.read(self.connection.PACKET_SIZE)
        bytes_sent = 0

        from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar
        self.pb = progressbar.ProgressBar("Sending file", "Sending: {}".format(filepath))
        self.pb.show()
        self.pb.setValue(0)

        while line:
            # if self.connection_encrypted == "true":
            #     line = self.rsaCrypt.encryptLine(line)

            self.socket.sendall(line)  # Send line
            bytes_sent += len(line)  # Add amount ob bytes sent to counter
            self.progressBar(bytes_sent, filesize)  # update progress bar
            line = filetosend.read(self.connection.PACKET_SIZE)  # get new line from file
        filetosend.close()

        self.socket.sendall(self.getmd5(filepath).encode())  # send md5 hash to server
        self.pb.close()

        if self.waitForServer("Succes"):  # wait for server to confirm md5 hash
            self.status = "Connected"
            return True
        else:
            print ("Error transfering file")
            self.status = "Connected"
            return False

    def receiveFile(self, filesize, filename, subDir):

        # create new queue for this file operation
        self.TransferQueue = queue.Queue()
        self.status = "Receiving File(s)"

        print("Receiving file!Size: {}b, Name: {}, Dir: {}".format(filesize, filename, subDir))
        bytes_received = 0
        save_file_path = utility.settings.settings["defaultSavePath"] + subDir + "\\" + filename

        print ("Curr thread id = {}".format(threading.current_thread().ident))
        self.sendInternalTransferMessage("accept")  # sends message to client to begin transfer

        with open(save_file_path, 'wb') as f:
            print('File opened. Beginning to save\n')
            while True:

                data = self.socket.recv(self.connection.PACKET_SIZE)
                if not data:
                    time.sleep(0.1)
                    continue

                f.write(data)
                bytes_received += len(data)

                # self.progressBar(bytes_received, filesize)
                if bytes_received >= filesize:
                    f.close()
                    self.status = "Connected"
                    if self.checkFileIntegrity(save_file_path):
                        self.sendInternalTransferMessage("Succes")
                        print('Successfully got the file\n')
                        return True
                    else:
                        self.sendInternalTransferMessage("Fail")
                        print('Error getting the file\n')
        f.close()
        return False

    def sendRawMessage(self, message):

        if self.connection.connection_encrypted == "true":
            message = self.connection.rsaCrypt.encryptLine(message)

        if isinstance(message, str):
            message = message.encode()

        self.socket.send(message)

    def sendInternalMessage(self, message):
        msg = ("-Internal" + self.connection.separator + message)
        if self.connection.connection_encrypted == "true":
            msg = self.connection.rsaCrypt.encryptLine(msg)
        else:
            msg = message.encode()
        self.socket.sendall(msg)

    def sendInternalTransferMessage(self, message):
        msg = ("-Internal" + self.connection.separator + "-transfer" + self.connection.separator + message)
        if self.connection.connection_encrypted == "true":
            msg = self.connection.rsaCrypt.encryptLine(msg)
        else:
            msg = message.encode()
        self.socket.sendall(msg)

    def findFileNameFromPath(self, file_path):
        list = file_path.split("\\")
        return list[-1]  # last element of the list

    def progressBar(self, bytesSent, baseSize):

        percentage = (bytesSent / baseSize) * 100
        percentage = round(percentage, 1)
        self.pb.setValue(percentage)

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

        for i in range (0,11): #wait for 10 sec
            if not self.TransferQueue.empty():
                message = self.TransferQueue.get()
                print ("waitForServer:message={}".format(message))
                if message == keyword:
                    return True
                else:
                    return False
            time.sleep(1)

    def getmd5(self, filepath):
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        print ("\n"
               "Client md5 for {}: {}".format(filepath, hash_md5.hexdigest()))
        return hash_md5.hexdigest()

    def checkFileIntegrity(self, filename):
        md5Server = self.getmd5(filename)  # gen md5

        timeout = 0
        while timeout < self.connection.valTimeout:  # wait for client to send its md5 hash
            data = self.socket.recv(1024)
            if data:
                md5Client = data.decode()  # get md5 from client
                if data:
                    print ("Expecting {} got {}".format(md5Server, md5Client))
                if md5Client == md5Server:  # compare md5 hashes
                    print ("MD5 match")
                    return True
                else:
                    print ("MD5 no match")
                    return False
            else:
                timeout += 1
                time.sleep(1)
        print ("Connection timed out")  # if failed to get md5 from server for 10sec

    def handleInternalQueue(self):
        while True:
            if self.InternalQueue and not self.InternalQueue.empty():
                receivedMessage = self.InternalQueue.get()
                message = receivedMessage.split(" ")
                self.connection.TransferQueue.put()
                if message[0] == "-transfer":
                    if self.connection.TransferQueue:
                        self.connection.TransferQueue.put(receivedMessage)
                        print ("Putting {} in file queue".format(receivedMessage[10:]))
                        self.connection.TransferQueue.put(
                            receivedMessage[10:])  # put all message excluding "-transfer "
            time.sleep(0.5)

    def shutdown(self):
        self.socket.shutdown()
