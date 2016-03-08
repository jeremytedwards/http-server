# -*- coding: utf-8 -*-
import socket

test_message = 'Worst case test message!'

def client(message=test_message):
    infos = socket.getaddrinfo('127.0.0.1', 5001)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]

    client_socket = socket.socket(*stream_info[:3])
    client_socket.connect(stream_info[-1])
    client_socket.sendall(message.encode('utf-8'))

    #waiting for response
    buffered_message = ""
    buffer_length = 4096
    client_socket.recv(buffer_length)
    message_complete = False
    while not message_complete:
        print('waiting for response')
        part = client_socket.recv(buffer_length)
        buffered_message += part.decode('utf-8')
        if len(part) < buffer_length:
            print(buffered_message)
            message_complete = True

#TODO: Accumulate any reply into a string
#TODO: Close socket and return message


# def main():
#     while True:
#         user_input = input('>>>')
#         try:
#             client(user_input)
#         except (IOError, KeyboardInterrupt):
#             client(close=True)

if __name__ == '__main__':
    client('This is like, our test')
    # main()
