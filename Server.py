import socket  # Import socket module
import os


PACKET_SIZE = 1024

def load_def_path():
    path_to_config = sys.argv[0]
    os.path.abspath(path_to_config)
    path_to_config = path_to_config.replace('bin/test.py','')
    path_to_config += "config\\client.cfg"

    with open(path_to_config) as f:
        name,value = (f.readline()).split(' ')
    close(f)

    return value

def main():


    port = 50000  # Reserve a port for your service every new transfer wants a new port or you must wait.
    host = "192.168.1.9"  # Get local machine name
    s = socket.socket()  # Create a socket object
    s.bind((host, port))  # Bind to the port
    s.listen(10)  # Now wait for client connection.



    print ("local ip: {}".format(host))

    while (1):
        bytes_received = 0 
    
        print ('Server listening....')
        sock, addr = s.accept()

        print("User connected at: {}".format(addr))
        received = sock.recv(1024)
        filename = received.decode()

        if filename == "-message":
            print("=============================================================")
            print("receiving message!")
            print("=============================================================")
            received = sock.recv(1024)
            filename = received.decode()
            print (filename)
            print("=============================================================")

        elif filename == "-file":

            print("receiving file!")
            received = sock.recv(1024)
            filename = received.decode()
            print("Received filename 1: {}".format(filename))

            filename = os.path.basename(filename)
            print("Received filename 2: {}".format(filename))

            received = sock.recv(1024)
            filesize = int(received.decode())

            progress_perc=0

            save_file_path = load_def_path() +  "\\" + filename

            with open(save_file_path, 'wb') as f:
                print('file opened')
                while True:
                    bytes_received += 1024

                    if (int((bytes_received / filesize) * 100)) > progress_perc:
                        print("\rProgress: {}/{} mb sent,{}%".format(round(bytes_received / 1000000, 2),round(filesize / 1000000, 2), progress_perc), end="\r")
                        progress_perc += 1

                    data = sock.recv(1024)
                    if not data:
                        break
                    f.write(data)

            f.close()
            print('Successfully get the file')
    s.close()
    print('connection closed')


main()
