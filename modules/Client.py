#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import socket
import sys
import time

PACKET_SIZE = 1024
SEPARATOR = "<SEPARATOR>"

def find_file_name_from_path(file_path):
    filename = ""

    i = len(file_path) - 1
    while file_path[i] != '/':
        i -= 1

    i += 1
    while i < len(file_path):
        filename += file_path[i]
        i += 1
    return filename

def Client_Send_File():

    send_mode = ""
    file_path = ""
    host = ""
    port = 0

    if len(sys.argv) < 4:
        print ("USAGE: -mode file_path port host")
        ### DEBUG ###
        send_mode = "-file"  # sending message or file?
        file_path = "C:/Users/kanton/Desktop/test_python_send.txt"
        host = "192.168.1.9"
        port = 50000
    else:
        send_mode = sys.argv[1]  # sending message or file?
        file_path = sys.argv[2]
        host = sys.argv[3]
        port = int(sys.argv[4])

    print ("mode: {}".format(send_mode))
    print ("file_path: {}".format(file_path))
    print ("host: {}".format(host))
    print ("port: {}".format(port))

    s = socket.socket()
    s.connect((host, port))


    #### BEGIN SEND FILE


    if send_mode == "-file":

        #s.send("-file".encode())

        filename = find_file_name_from_path(file_path)
        filesize = int(os.path.getsize(file_path))

        print("File size: {} mb".format(round(filesize/1000000,2)))
        print("sending file name: {}".format(filename))



        s.send((f"{send_mode}{SEPARATOR}{filename}{SEPARATOR}{filesize}").encode())

        # start sending the file
        f = open(file_path, 'rb')
        l = f.read(PACKET_SIZE)

        print ("==============================================")
        print ("Starting the transfer")
        print ("==============================================")
        bytes_sent = 0
        while (l):
            s.sendall(l)
            bytes_sent += PACKET_SIZE

            se_bytes = round(bytes_sent / 1000000,2)
            se_file_size = round(filesize / 1000000,2)
            se_perc = round(((bytes_sent / filesize) *100),2)
            print("\rProgress: {:.2f}/{} mb sent,{}%".format(se_bytes, se_file_size,se_perc), end="\r")

            l = f.read(PACKET_SIZE)
        f.close()
        s.close()

        time.sleep(2)


        #### END SEND FILE


    elif send_mode == "-message":
        s.send(("{send_mode}{<SEPARATOR}{file_path}{SEPARTOR}{NULL}"))

# host = "192.168.1.9"
# port = 50000
# file_path = "C:\\Users\\kanton\\Desktop\\serverv2.py"

Client_Send_File()
