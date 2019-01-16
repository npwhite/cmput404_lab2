#!/usr/bin/env python3
import socket
import logging
import sys
logging.basicConfig(format='%(levelname)s:%(message)s', stream=sys.stderr, level=logging.DEBUG)

HOST = "www.google.com"
PORT = 80
BUFFER_SIZE = 1024

# payload = """GET / HTTP/1.0
# Host: {HOST}
# """.format(HOST=HOST)
payload = "GET / HTTP/1.0\r\n\r\n"

def conn_socket(addr_tup):
    (family, socktype, proto, canonname, sockaddr) = addr_tup
    print(proto)
    try:
        s = socket.socket(family, socktype, proto)
        s.connect(sockaddr)
        s.sendall(payload.encode())
        #s.sendall(payload)

        full_data = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            #print(data)
            if not data:
                break
            full_data += data

        #print(full_data)
    except Exception as e:
        print(e)
        pass
    finally:
        s.close()

def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
    addr_tup = addr_info[0]
    logging.debug('addr_tup = {}'.format(addr_tup))

    conn_socket(addr_tup)

if __name__ == "__main__":
    main()
