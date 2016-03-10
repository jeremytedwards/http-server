# -*- coding: utf-8 -*-

import pytest

# the server must not be running for this test


def test_response_template():
    pass


ERROR_RESPONSE = [
    ("200", u"HTTP/1.1 200 OK\r\n"),
    ("400", u"HTTP/1.1 400 Bad Request\r\n"),
    ("404", u"HTTP/1.1 404 File Not Found\r\n"),
    ("405", u"HTTP/1.1 405 Method Not Allowed\r\n"),
    ("500", u"HTTP/1.1 500 Internal Server Error\r\n"),
    ("505", u"HTTP/1.1 505 HTTP Version Not Supported\r\n"),
]


@pytest.mark.parametrize("error, response", ERROR_RESPONSE)
def test_response_check(error, response):
    from server import response_check
    assert response_check(error) == response
