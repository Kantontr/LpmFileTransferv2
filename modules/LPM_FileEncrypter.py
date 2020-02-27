import os
import sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


def split_extension(string):

    int_extension = 0
    for i in range(len(string) - 1, 0, -1):
        if string[i] == '.':
            break
        int_extension += 1

    extension = string[len(string) - 1 - int_extension:len(string)]
    file_path = string[0:len(string) - 1 - int_extension] + "(enc)" + extension
    return file_path, extension


def encrypt(key, filename, s_mode, password):

    chunksize = 64 * 1024
    outputFile, extension = split_extension(filename)

    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = Random.new().read(16)

    encryptor = AES.new(key, AES.MODE_CBC, IV)
    bool_error = False

    try:
        with open(filename, 'rb') as infile:
            with open(outputFile, 'wb') as outfile:
                outfile.write(filesize.encode('utf-8'))
                outfile.write(IV)

                if s_mode == "-s":
                    try:
                        s_chunk = str(password).zfill(16)
                        s_chunk = s_chunk.encode('utf-8')
                        outfile.write(encryptor.encrypt(s_chunk))
                        print ("Safe mode: {}".format(s_chunk))

                    except:
                        print ("Fatal error creating safe mode!")
                        sys.exit()

                while True:
                    chunk = infile.read(chunksize)

                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - (len(chunk) % 16))

                    outfile.write(encryptor.encrypt(chunk))
    except:
        bool_error = True

    if os.path.exists(outputFile) and bool_error == False:
        os.remove(filename)


def decrypt(key, filename, s_mode, password):
    chunksize = 64 * 1024
    outputFile, extension = split_extension(filename)
    outputFile = outputFile[0:len(filename) - 9] + extension

    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))
        IV = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, IV)

        if s_mode == "-s":
            s_chunk = str(password).zfill(16)
            s_chunk = s_chunk.encode('utf-8')

            s_password = infile.read(16)
            s_password = decryptor.decrypt(s_password)

            if s_password != s_chunk:
                print("Error decoding with safe mode!")
                print ("comp {} to {}".format(s_password, s_chunk))
                sys.exit()

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)

    if os.path.exists(outputFile):
        os.remove(filename)


def getKey(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()


def Main():
    # usage: <filepath> <flag>(-e -d) <password> <s_mode> (-s -is)


    try:

        filename = sys.argv[1]
        mode = sys.argv[2]
        s_mode = sys.argv[3]

        if len(sys.argv) < 5:
            if (sys.argv[2] == "-d" or sys.argv[2] == "-e") and (sys.argv[3] == "-s" or sys.argv[3] == "-is"):
                password = input("Type your password: ")
        else:
            password = sys.argv[4]
    except:
        print ("Invalid arguments!")
        print ("Usage: <filepath> <flag>(-e -d) <s_mode>(-s -is) <password>(optional)")
        sys.exit()

    if mode == '-e':
        encrypt(getKey(password), filename, s_mode, password)
        print("Done encrypting: {}".format(filename))
    elif mode == '-d':
        decrypt(getKey(password), filename, s_mode, password)
        print("Done decrypting: {}".format(filename))
    else:
        print("No Option selected, closing...")


if __name__ == '__main__':
    Main()
