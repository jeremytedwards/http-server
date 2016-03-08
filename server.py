# -*- coding: utf-8 -*-

import socket

def server():
    server_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM,
                                  socket.IPPROTO_TCP,)
    print("\nserver: ", server_socket)
    address = ('127.0.0.1', 5001)
    server_socket.bind(address)
    print("\nserver: ", server_socket)
    server_socket.listen(1)
    print("\nlistening...")
    listening = True

    
    while listening:
        conn, addr = server_socket.accept()
        # Receive the buffered message
        buffered_message = ""
        buffer_length = 4096
        message_complete = False
        while not message_complete:
            try:
                part = conn.recv(buffer_length)
                buffered_message += part.decode('utf-8')
                if len(part) == 0:
                    listening = False
                    break
                else:
                    if len(part) < buffer_length:
                        conn.sendall(buffered_message.encode('utf-8'))
                        print(buffered_message)
                        message_complete = True
            except KeyboardInterrupt:
                conn.close()
                print('connection closed')
                server.close()
                print('server closed')


# TODO: When the Client hits Ctrl+D then the connection closes

server()
