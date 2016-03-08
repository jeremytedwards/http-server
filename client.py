# -*- coding: utf-8 -*-
import socket

test_message = 'Worst case test message!'

def client(message=test_message):
    infos = socket.getaddrinfo('127.0.0.1', 5000)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]

    client_socket = socket.socket(*stream_info[:3])
    client_socket.connect(stream_info[-1])
    client_socket.sendall(message.encode('utf-8'))

    #waiting for response
    buffered_message = ""
    buffer_length = 4096

    while True:
        part = client_socket.recv(buffer_length)
        buffered_message += part.decode('utf-8')
        if len(part) < buffer_length:
            print(buffered_message)
            # client_socket.close()


def main():
    while True:
        user_input = input('>>>')
        client(user_input)

if __name__ == '__main__':
    main()
