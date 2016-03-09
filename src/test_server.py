# -*- coding: utf-8 -*-

import pytest

# the server must not be running for this test
def test_response_ok():
    from server import response_ok
    ok_output = response_ok()
    assert ok_output[0] == "HTTP/1.1 200 OK\n"
    assert ok_output[2] == "Content-type: text/html; charset=utf-8\n"


def test_response_error():
    from server import response_error
    error_output = response_error()
    assert error_output[0] == "HTTP/1.1 500 Internal Server Error\n"
    assert error_output[2] == "Content-type: text/html; charset=utf-8\n"
