import os
import socket
import sys
import time
import hashlib
from . import LPMRsaEncrypt
from modules import progressbar


class ClientConnection:
    def __init__(self, name, ip, port):
        self.connection_name = name
        self.connection_ip = ip
        self.connection_port = port
        self.PACKET_SIZE = 2048
        self.separator = "<S3P4>"
        self.valTimeout = 60.0
        self.s = None
        self.connection_encrypted = "true"
        self.connection_status = "connecting"
        self.rsaCrypt = LPMRsaEncrypt.LPMRsaEncrypt(self.PACKET_SIZE)
        if self.createConnection():
            self.s.settimeout(self.valTimeout)
            if self.connection_encrypted == "true":
                try:
                    self.encryptConnection()
                except:
                    self.connection_status = "error encrypting"
                    pass
            else:
                self.connection_status = "Online"

    def __del__(self):
        self.connection_status = "Offline"
        print ("Deconstructor called. Ending connection with {}:{}".format(self.connection_ip, self.connection_port))


    def createConnection(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.connection_ip, int(self.connection_port)))
            print ("Connection with {}:{} initialized".format(self.connection_ip, self.connection_port))
            self.connection_status = "Initialized"
            return True
        except:
            print ("Connection with {}:{}  could not be initialized".format(self.connection_ip, self.connection_port))
            self.connection_status = "error"
            return False

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
            self.connection_status = "Online"
            return True
        else:
            self.connection_status = "error"
            return False

    def sendRawMessage(self, message):

        if self.connection_encrypted == "true":
            message = self.rsaCrypt.encryptLine(message)

        if isinstance(message, str):
            message = message.encode()

        self.s.send(message)


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

    def endConnection(self):
        msg = "CloseSocket" + self.separator
        try:
            self.s.send(msg.encode('utf-8'))
            self.s.close()
            print ("Connection with {} closed".format(self.connection_ip))
        except:
            print ("Connection with {} already closed".format(self.connection_ip))
        finally:
            self.connection_status = "Offline"
