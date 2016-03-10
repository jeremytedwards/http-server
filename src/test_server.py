# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

# the server must not be running for this test


def test_response_template():
    from server import response_template
    response = response_template()
    assert 'Content-length: \r\n\r\n' in response


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


FAILED_MESSAGES = [
    (u"SET / HTTP/1.1\r\nHost: localhost:5000", NameError),
    (u"GET / HTTP/1.0\r\nHost: localhost:5000", TypeError),
    (u"GET / HTTP/1.1\r\nNo Host", ValueError)
]

SUCCESS_MESSAGE = [(u"GET / HTTP/1.1\r\nHost: localhost:5000", "/")]


@pytest.mark.parametrize("error, response", FAILED_MESSAGES)
def test_parse_request_failed(error, response):
    from server import parse_request
    with pytest.raises(response):
        assert parse_request(error) == response


@pytest.mark.parametrize("error, response", SUCCESS_MESSAGE)
def test_parse_request_success(error, response):
    from server import parse_request
    assert parse_request(error) == response
