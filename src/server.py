# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import OrderedDict

import socket
import email.utils


def response_ok():
    return ["HTTP/1.1 200 OK",
            str("Date: " + email.utils.formatdate(usegmt=True)),
            "Content-type: text/plain; charset=utf-8",
            "Content-length: \n",
            "Body: "]



# def response_error():
#     return "HTTP/1.1 500 Internal Server Error" \
#            "Date: Wed, 30 Jul 2014 15:11:42 GMT" \
#            "Content-type: application/soap+xml; charset=utf-8" \
#            "Content-length:" \


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
            msg_response = response_ok()
            buffer_length = 8
            while True:
                part = conn.recv(buffer_length)
                msg_response[4] += part.decode('utf-8')

                if len(part) < buffer_length:
                    # Get length
                    msg_response[3] = "Content-length: " + str(len(msg_response[4])) + "\n"

                    # loop through and send each item
                    # conn.sendall(buffered_message_dict.encode('utf-8'))
                    # for i in buffered_message_dict:
                    #     conn.send(i)

                    for c in msg_response:
                        print(c)
                    break
            conn.close()

    except KeyboardInterrupt:
        conn.close()
        print('connection closed')
        server.close()
        print('server closed')

server()

# TODO: When the Client hits Ctrl+D then the connection closes