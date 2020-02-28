import os.path
import sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


class LPM_Encryptor:
    password = ""
    key = ""
    s_mode = "-s"

    # For encryption
    val_fill = 16
    enc_IV = ...
    dec_IV = ...
    encryptor = ...
    decryptor = ...

    def __init__(self):
        pass

    def setPassword(self, pswd):
        self.password = pswd
        self.key = self.getKey(pswd)
        self.gen_enc()

    def gen_enc(self):
        self.enc_IV = Random.new().read(self.val_fill)
        self.encryptor = AES.new(self.key, AES.MODE_CBC, self.enc_IV)

    def gen_dec(self, new_dec_IV):
        self.dec_IV = new_dec_IV
        self.decryptor = AES.new(self.key, AES.MODE_CBC, self.dec_IV)

    def getKey(self, password):
        hasher = SHA256.new(password.encode('utf-8'))

        return hasher.digest()

    def removeBfromline(self, line):
        corr_line = ""
        i=0
        while i< len(line):
            corr_line += line[i + 2:i + 18]
            #print("zmiana na {}".format(line[i + 2:i + 18]))
            i += 19

        return corr_line

    def fill_and_encrypt(self, line):

        chunk = str(line).zfill(self.val_fill)
        chunk = chunk.encode('utf-8')

        if len(chunk) % self.val_fill != 0:
            chunk += b' ' * (self.val_fill - (len(chunk) % self.val_fill))

        return self.encryptor.encrypt(chunk)

    def encrypt_line(self, line):
        # adds size + fill and encrypt

        line_len = len(line)
        return_val = self.fill_and_encrypt(line_len)

        char_counter = 0
        while True:
            if line_len - char_counter > 16:
                return_val += self.fill_and_encrypt(line[char_counter:char_counter + 16])
                char_counter += 16
            else:
                return_val += self.fill_and_encrypt(line[char_counter:line_len])
                return return_val

    def decrypt_line(self, line):

        encrypted_line = line
        return_val = ""
        len_line = len(encrypted_line)
        len_processed = 0

        while True:

            if len_processed == len_line:
                return self.removeBfromline(return_val)

            tmp = encrypted_line[len_processed:len_processed + 16]
            line_decrypted = self.decryptor.decrypt(tmp)
            return_val += str(line_decrypted)
            len_processed += 16
