#!/usr/bin/env python3

# references
# https://docs.python.org/3.5/library/socket.html#example

# lab solution
import socket
import time
from multiprocessing import Process

HOST = ""
PORT = 8081
BUFFER_SIZE = 1024

def handle_echo(conn, addr):
    with conn:
        print(conn)
        full_data = b""
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            full_data += data
        time.sleep(0.5)
        conn.sendall(full_data)


def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))

        s.listen(1)

        while True:
            conn, addr = s.accept()
            p = Process(target=handle_echo, args=(conn, addr))
            p.daemon = True
            p.start()
            print("Started process: ", p)

if __name__ == "__main__":
    main()







# # ------------------------------------
# # My solution
# import socket
#
# HOST = ''
# PORT = 8001
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     # socket.setsockopt(level, optname, value)
#     s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     s.bind((HOST, PORT))
#     s.listen(1)
#     print("Listening...")
#
#     # addr is pair (host, port) where port is the port used by client
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         data = conn.recv(1024)
#         print("Server Side: {}".format(data))
#         conn.sendall(data)
