import os.path
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

class LPMRsaEncrypt:

    def __init__(self):
        self.encryptor = None
        self.decryptor = None
        self.keyPair = RSA.generate(1024)
        self.pubKey = self.keyPair.publickey()
        self.pubKeyPEM = self.pubKey.exportKey()
        self.privKeyPEM = self.keyPair.exportKey()

        self.setEncryptor(self.pubKeyPEM)
        self.setDecryptor()

    def setEncryptor(self,pubKey):
        self.encryptor = PKCS1_OAEP.new(RSA.importKey(pubKey))
        print ("Successfull")

    def setDecryptor(self):
        self.decryptor = PKCS1_OAEP.new(self.keyPair)

    def encryptLine(self, line):
        encrypted = self.encryptor.encrypt(line)
        return encrypted

    def getPublicKey(self):
        return str(self.keyPair.publickey().exportKey(format='PEM'), "utf-8")
        #return self.pubKey

    def decryptLine(self, line):
        decrypted = self.decryptor.decrypt(line)
        return str(decrypted.decode())

    def getInfo(self):
        print ("My Pubkey is: {} \n".format(self.pubKey))