import socket  # Import socket module
import os
import time
import sys
import hashlib
from . import LPMRsaEncrypt
from modules import utility


class ServerConnection:

    def __init__(self, ip, port):
        self.connection_ip = utility.settings.settings["serverIp"]
        self.connection_port = int(utility.settings.settings["serverPort"])
        self.connection_ip = ip
        self.connection_port = port
        self.PACKET_SIZE = 2048
        self.separator = "<S3P4>"
        self.valTimeout = int(utility.settings.settings["serverRequestTimeout"])
        self.connection_encrypted = "false"
        self.defaultSaveFilePath = utility.settings.settings["defaultSavePath"]
        self.rsaCrypt = LPMRsaEncrypt.LPMRsaEncrypt(self.PACKET_SIZE)
        self.createConnection()
        self.s.settimeout(self.valTimeout)
        self.waitForConnection()

    def __del__(self):
        self.s.close()

    def createConnection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
        print ("Starting server on {} {}".format(self.connection_ip, self.connection_port))
        self.s.bind((self.connection_ip, self.connection_port))  # Bind to the port

    def waitForConnection(self):
        try:
             # Reset values from previous connection:
            self.connection_encrypted = "false"
            self.rsaCrypt = LPMRsaEncrypt.LPMRsaEncrypt(self.PACKET_SIZE)
            # wait for client connection.
            self.s.listen(10)
            print ('Server listening...')
            # Creating new connection
            self.sock, self.addr = self.s.accept()
            print("User connected at: {}".format(self.addr))
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

    def sendMessage(self, message):
        print("Sending {} to {}".format(message, self.addr))
        self.sock.sendall(message.encode())

    def sendRawMessage(self, message):

        if self.connection_encrypted == "true":
            message = self.rsaCrypt.encryptLine(message)

        if isinstance(message, str):
            message = message.encode()

        self.sock.send(message)

    def endConnection(self):
        print("Connection with {} closed".format(self.addr))
        self.s.close()
        self.createConnection()
        self.waitForConnection()
