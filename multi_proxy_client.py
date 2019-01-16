#!/usr/bin/env python3
import socket
from multiprocessing import Pool

HOST = ""
PORT = 8081
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\n\r\n"

def conn_socket(addr_tup):
    (family, socktype, proto, canonname, sockaddr) = addr_tup
    try:
        s = socket.socket(family, socktype, proto)
        s.connect(sockaddr)
        #print("sending...")
        s.sendall(payload.encode())
        #print("sent")

        # shut down writing on the client side
        s.shutdown(socket.SHUT_WR)

        full_data = b""
        while True:
            #print("before recv")
            data = s.recv(BUFFER_SIZE)
            #print("after recv")

            if not data:
                break
            full_data += data

        print(full_data)
    except Exception as e:
        print(e)
    finally:
        #print("closing socket...")
        s.close()

def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
    #print(addr_info)
    addr_tup = addr_info[1]
    with Pool() as p:
        p.map(conn_socket, [addr_tup for _ in range(10)])
    # for i in range(10):
    #     conn_socket(addr_tup)


        # conn_socket(addr_tup)
        # only ipv4 I guess

if __name__ == "__main__":
    main()
