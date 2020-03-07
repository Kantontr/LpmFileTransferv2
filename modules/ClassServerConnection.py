import socket  # Import socket module
import os
import time
import sys
import hashlib
from . import LPMRsaEncrypt


class ServerConnection:

    def __init__(self, ip, port, SaveFilePath):
        self.connection_ip = ip
        self.connection_port = port
        self.PACKET_SIZE = 2048
        self.separator = "<S3P4>"
        self.valTimeout = 20.0
        self.connection_encrypted = "false"
        self.defaultSaveFilePath = SaveFilePath
        self.rsaCrypt = LPMRsaEncrypt.LPMRsaEncrypt(self.PACKET_SIZE)
        self.createConnection()
        self.s.settimeout(self.valTimeout)
        self.waitForConnection()

    def __del__(self):
        s.close()


    def createConnection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
        print ("Starting server on {} {}".format(self.connection_ip, self.connection_port))
        self.s.bind((self.connection_ip, self.connection_port))  # Bind to the port

    def waitForConnection(self):
        try:
            while True:  # Keep server on until turned off by user
                # Reset values from previous connection:
                self.connection_encrypted = "false"
                self.rsaCrypt = LPMRsaEncrypt.LPMRsaEncrypt(self.PACKET_SIZE)
                # wait for client connection.
                self.s.listen(10)
                print ('Server listening...')
                #Creating new connection
                self.sock, self.addr = self.s.accept()
                print("User connected at: {}".format(self.addr))
                self.handleIncomingMessage()
        except:
            self.endConnection()

    def encryptConnection(self):

        # Send server's public key to client
        self.sock.send(self.rsaCrypt.getPublicKey().encode())
        print ("Server public key sent.")

        # Wait for Client's public key
        clientPublicKey = self.sock.recv(self.PACKET_SIZE)
        print ("Client public key received!")
        self.rsaCrypt.setEncryptor(clientPublicKey.decode())

        # Wait for encoded hand shake
        msgEnc = self.sock.recv(self.PACKET_SIZE)
        msg = self.rsaCrypt.decryptLine(msgEnc)
        print ("Got {} from client".format(msg))

        if msg == "clienthandshake":
            print ("Accepting client's handshake")
            self.sock.send(self.rsaCrypt.encryptLine("Returning handshake"))
            print ("Returning handshake. \nConnection established")
            self.connection_encrypted = "true"
            return True
        else:
            return False

    def handleIncomingMessage(self):
        while True:
            received = self.sock.recv(self.PACKET_SIZE)

            if self.connection_encrypted == "true":
                message = self.rsaCrypt.decryptLine(received)
            else:
                message = str(received.decode())

            receivedMessage = message.split(self.separator)
            mode = receivedMessage[0]  # get mode from message
            print ("Message inbound {}".format(receivedMessage))
            print ("Mode: {}".format(mode))

            if mode == "-File":
                self.receiveFile(int(receivedMessage[1]), receivedMessage[2], receivedMessage[3])
            elif mode == "CloseSocket":
                self.endConnection()
                return
            elif mode == "ConnectionCheck":
                print ("got connection check request")
                self.sendMessage("ConnectionEstablished")
            elif mode == "EncryptConnection":
                print ("Encrypting connection")
                self.encryptConnection()

            print ('Server listening...')

    def receiveFile(self, filesize, filename, dirpath):
        print("Receiving file!Size: {}b, Name: {}, Dir: {}".format(filesize, filename, dirpath))
        bytes_received = 0
        save_file_path = self.defaultSaveFilePath + dirpath + "\\" + filename

        self.sendRawMessage("ready")  # sends message to client to begin transfer
        with open(save_file_path, 'wb') as f:
            print('File opened. Beginning to save\n')
            while True:

                data = self.sock.recv(self.PACKET_SIZE)
                if not data:
                    break

                # if self.connection_encrypted == "true":
                #     data = self.rsaCrypt.decryptLine(data)

                f.write(data)
                bytes_received += len(data)

                self.progressBar(bytes_received, filesize)
                if bytes_received >= filesize:
                    f.close()
                    if self.checkFileIntegrity(save_file_path):
                        self.sendRawMessage("Succes")
                        # self.sendMessage("Succes")
                        print('Successfully got the file\n')
                        return True
                    else:
                        self.sendRawMessage("Fail")
                        # self.sendMessage("Fail")
                        print('Error getting the file\n')
        f.close()
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

    def checkFileIntegrity(self, filename):
        md5Server = self.getmd5(filename)  # gen md5

        timeout = 0
        while timeout < self.valTimeout:  # wait for client to send its md5 hash
            data = self.sock.recv(1024)
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

    def sendMessage(self, message):
        print("Sending {} to {}".format(message, self.addr))
        self.sock.sendall(message.encode())

    def sendRawMessage(self, message):

        if self.connection_encrypted == "true":
            message = self.rsaCrypt.encryptLine(message)

        if isinstance(message, str):
            message = message.encode()

        self.sock.send(message)

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
