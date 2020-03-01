import socket  # Import socket module
import os
import time


class ServerConnection:

    def __init__(self, ip, port, SaveFilePath):
        self.connection_ip = ip
        self.connection_port = port
        self.defaultSaveFilePath = SaveFilePath
        self.createConnection()
        self.waitForConnection()

    defaultSaveFilePath = None
    PACKET_SIZE = 1024
    separator = "<SEPARATOR>"
    connection_ip = None
    connection_port = None
    s = None
    sock = None
    addr = None

    def createConnection(self):
        self.s = socket.socket()  # Create a socket object
        self.s.bind((self.connection_ip, self.connection_port))  # Bind to the port
        self.s.listen(10)  # Now wait for client connection.

    def waitForConnection(self):
        print ('Server listening....')
        self.sock, self.addr = self.s.accept()
        print("User connected at: {}".format(self.addr))
        self.handleIncomingMessage()

    def handleIncomingMessage(self):
        while True:
            received = self.sock.recv(1024)
            if not received:
                time.sleep(0.2)
                continue
            message = str(received)

            receivedMessage = message.split(self.separator)
            receivedMessage[0] = receivedMessage[0][2:]  # delete "b from message

            print ("First arg: {}".format(receivedMessage[0]))

            if len(receivedMessage)==4:
                print("MSG= {} {} {} {}".format(receivedMessage[0], int(receivedMessage[1]), receivedMessage[2],
                                            receivedMessage[3]))

            if receivedMessage[0] == "-f":
                self.receiveFile(int(receivedMessage[1]), receivedMessage[2], receivedMessage[3])
            elif receivedMessage[0] == "CloseSocket'":
                self.endConnection()
                return

            print ('Server listening....')

    def receiveFile(self, filesize, filename, dirpath):
        print("Receiving file!Size: {}, Name: {}, Dir: {}".format(filesize, filename, dirpath))

        bytes_received = 0
        save_file_path = self.defaultSaveFilePath + dirpath + "\\" + filename

        with open(save_file_path, 'wb') as f:
            print('file opened')
            while True:

                data = self.sock.recv(1024)
                if not data:
                    break
                f.write(data)
                bytes_received += len(data)

                self.progressBar(bytes_received, filesize)
                if bytes_received >= filesize:
                    print('Successfully got the file')
                    f.close()
                    return

        f.close()
        print('Successfully got the file')
        return True

    def progressBar(self, bytesSent, baseSize):
        v1 = round((bytesSent / baseSize) * 100, 1)
        print("\rProgress: {}/{} mb sent,{}%".format(bytesSent, baseSize, v1), end="\r")

    def endConnection(self):
        print("Connection with {} closed".format(self.addr))
        self.s.close()
