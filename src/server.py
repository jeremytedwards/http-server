# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import socket
import email.utils
import mimetypes
import io
import os

sample_template = (
    "<!DOCTYPE html>"
    "<html>"
    "<body>"
    "<h1>Code Fellows</h1>"
    "{body}"
    "</body>"
    "</html>"
)
def build_file_structre_html(src):
    return_value = sample_template
    for item in os.listdir(src):
        body = "<a href={item}/>{item}</a><br />".format(item)
    print(return_value.format(body))
    return return_value.format(body)


def response_template():
    return [u"",
            u"" + str("Date: " + email.utils.formatdate(usegmt=True) + "\r\n"),
            u"Content-type: text/html; charset=utf-8\r\n",
            u"Content-length: \r\n\r\n",
            b"Body: "]


def response_check(error):
    response_dict = {
        "200": u"HTTP/1.1 200 OK\r\n",
        "400": u"HTTP/1.1 400 Bad Request\r\n",
        "404": u"HTTP/1.1 404 File Not Found\r\n",
        "405": u"HTTP/1.1 405 Method Not Allowed\r\n",
        "500": u"HTTP/1.1 500 Internal Server Error\r\n",
        "505": u"HTTP/1.1 505 HTTP Version Not Supported\r\n",
    }
    return response_dict[error]


def parse_request(request):
    split_request = request.split('\r\n')
    request_list = split_request[0].split(' ')
    if request_list[0] == 'GET':
        if request_list[2] == 'HTTP/1.1':
            if 'Host: localhost:' in split_request[1]:
                return request_list[1]
            else:
                raise ValueError
        else:
            raise TypeError
    else:
        raise NameError


def handle_listening(conn):
    buffer_length = 4096
    byte_msg = b''
    while True:
        part = conn.recv(buffer_length)
        byte_msg += part
        if len(part) < buffer_length:
            decoded_msg = byte_msg.decode('utf-8')
            break
    return decoded_msg


def response_ok(body, type):
    response = response_template()
    response[0] = response_check("200")
    response[2] = u"Content-type: " + type + "; charset=utf-8\r\n"
    response[4] = body
    return response


def resolve_uri(uri):
    """
    returns a body and type based on uri as a tuple
    """
    os.chdir("webroot")
    path_to_root = os.path.join(os.getcwd(), uri)
    print("path to root: ", path_to_root)
    file_type = ""
    try:
        if os.path.isfile(path_to_root):
            print("is a file")
            filepath = io.open(path_to_root, 'rb')
            print("filepath :", filepath)
            body = filepath.read()
            print("body", body)
            file_type = mimetypes.guess_type(uri)
            print("file_type :", file_type)
            return body, file_type
        elif os.path.isdir(uri):
            print("is a directory")
            # return build_file_structre_html(uri), file_type
            return sample_template, file_type
            # show file system
    except OSError:
        pass
        # throw 404


def send_response(conn, response):
    for c in response:
        conn.send(c.encode('utf-8'))


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP,)
    print("\nserver: ", server_socket)

    address = ('127.0.0.1', 5001)
    server_socket.bind(address)
    print("\nserver: ", server_socket)

    server_socket.listen(1)
    print("\nlistening...")

    conn = None

    try:
        while True:
            conn, addr = server_socket.accept()
            try:
                while True:
                    # listen on socket
                    client_request = handle_listening(conn)
                    if client_request:
                        # TODO: uri could be an error handle it.
                        uri = parse_request(client_request)
                        body, file_type = resolve_uri(uri)
                        print("body :", body)
                        print("file_type :", file_type)
                        client_response = response_ok(body, file_type)

                        # Send the message
                        send_response(conn, client_response)
                    else:
                        conn.shutdown(socket.SHUT_RDWR)
                        break
            finally:
                conn.close()
    except KeyboardInterrupt:
        if conn is not None:
            conn.close()
        print('connection closed')
    finally:
        server_socket.close()
        print('server closed')


if __name__ == '__main__':
    server()
