from json import dumps
from socket import (
    socket,
    AF_INET,
    SOCK_STREAM,
)
from sys import argv

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    sock = socket(AF_INET, SOCK_STREAM)
    data = dumps([int(a) for a in argv[1:3]])

    try:
        sock.connect((HOST, PORT))
        sock.sendall((data + "\n").encode())

        received = sock.recv(1024).decode()
    finally:
        sock.close()

    print("Sent: {}".format(data))
    print("Received: {}".format(received))
