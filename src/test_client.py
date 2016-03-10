# -*- coding: utf-8 -*-

import pytest
# the server must be running for this test


CLIENT_MESSAGES = [
(u'GET / HTTP/1.1\r\nHost: localhost:5000\r\n', u'test string'),
(u'SET / HTTP/1.1\r\nHost: localhost:5000\r\n', u''),
(u'DELETE / HTTP/1.1\r\nHost: localhost:5000\r\n', u''),
(u'UPDATE / HTTP/1.1\r\nHost: localhost:5000\r\n', u'')
]


@pytest.mark.parametrize('request , response', CLIENT_MESSAGES)
def test_client_request(capfd, request, response):
    from client import client
    client(request)
    out, err = capfd.readouterr()
    assert response == out
