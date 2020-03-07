import os.path
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


class LPMRsaEncrypt:

    def __init__(self,keyLen):
        self.keyPair = RSA.generate(keyLen)
        self.pubKey = self.keyPair.publickey()
        self.setEncryptor(self.getPublicKey())
        self.setDecryptor()
        # Max message len is 86 if 1024b and 214 if 2048

    def setEncryptor(self, pubKey):
        self.encryptor = PKCS1_OAEP.new(RSA.importKey(pubKey))

    def setDecryptor(self):
        self.decryptor = PKCS1_OAEP.new(self.keyPair)

    def encryptLine(self, line):  # gets str or byte returns byte

        if isinstance(line, str):
            line = line.encode()

        encrypted = self.encryptor.encrypt(line)
        return encrypted

    def decryptLine(self, line):
        decrypted = self.decryptor.decrypt(line)
        return str(decrypted.decode())

    def getPublicKey(self):
        return str(self.keyPair.publickey().exportKey(format='PEM'), "utf-8")
