# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import socket


def response_ok():
    return "HTTP/1.1 200 OK"


def response_error():
    return "HTTP/1.1 500 Internal Server Error"


def server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP,)
        print("\nserver: ", server_socket)

        address = ('127.0.0.1', 5001)
        server_socket.bind(address)
        print("\nserver: ", server_socket)

        while True:
            server_socket.listen(1)
            print("\nlistening...")

            conn, addr = server_socket.accept()

            # Receive the buffered message
            buffered_message = ""
            buffer_length = 8
            while True:
                part = conn.recv(buffer_length)
                buffered_message += part.decode('utf-8')
                if len(part) < buffer_length:
                    conn.sendall(buffered_message.encode('utf-8'))
                    print(buffered_message)
                    break
            conn.close()

    except KeyboardInterrupt:
        conn.close()
        print('connection closed')
        server.close()
        print('server closed')

server()

# TODO: When the Client hits Ctrl+D then the connection closes
