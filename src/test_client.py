# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

# the server must be running for these tests

CLIENT_MESSAGES = [
    (u"GET / HTTP/1.1\r\nHost: localhost:5000\r\n", u"test string"),
    (u'SET / HTTP/1.1\r\nHost: localhost:5000\r\n', u''),
    (u'DELETE / HTTP/1.1\r\nHost: localhost:5000\r\n', u''),
    (u'UPDATE / HTTP/1.1\r\nHost: localhost:5000\r\n', u''),
]


@pytest.mark.parametrize("req, resp", CLIENT_MESSAGES)
def test_client_request(req, resp):
    from client import client
    assert client(req) == resp
