# -*- coding: utf-8 -*-

import pytest

MSG_TABLE = [
    (u'This message is longer', u'This message is longer\n'),
    (u'shorter', u'shorter\n'),
    (u'exactlen', u'exactlen\n'),
    (u'üñ cool', u'üñ cool\n')
]


# the server must be running for this test
@pytest.mark.parametrize('test_string, response', MSG_TABLE)
def test_client_shorter_than_buffer(test_string, response, capfd):
    from client import client
    client(test_string)
    out, err = capfd.readouterr()
    assert out == response


# the server must not be running for this test
def test_response_ok():
    from server import response_ok
    ok_output = response_ok()
    assert ok_output[0] == "HTTP/1.1 200 OK"
    assert ok_output[2] == "Content-type: text/html; charset=utf-8"


def test_response_error():
    from server import response_error
    error_output = response_error()
    assert error_output[0] == "HTTP/1.1 500 Internal Server Error"
    assert error_output[2] == "Content-type: text/html; charset=utf-8"
