#!/usr/bin/env python3

# references
# https://docs.python.org/3.5/library/socket.html#example

# lab solution
import socket

HOST = ""
PORT = 8081
BUFFER_SIZE = 1024

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)


        while True:
            conn, addr = s.accept()
            with conn:
                print(conn)
                print(addr)
                full_data = b""
                while True:
                    data = conn.recv(BUFFER_SIZE)
                    if not data:
                        break
                    full_data += data

                conn.sendall(full_data)

if __name__ == "__main__":
    main()
