#!/usr/bin/env python3
import socket

HOST = ""
PORT = 8081
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\n\r\n"


def conn_socket(addr_tup):
    (family, socktype, proto, canonname, sockaddr) = addr_tup
    try:
        s = socket.socket(family, socktype, proto)
        s.connect(sockaddr)
        s.sendall(payload.encode())

        # shut down writing on the client side
        s.shutdown(socket.SHUT_WR)

        full_data = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            full_data += data

        print(full_data)
    except e:
        print(e)
    finally:
        s.close()

def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
    addr_tup = addr_info[1]
    conn_socket(addr_tup)

if __name__ == "__main__":
    main()
