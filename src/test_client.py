# -*- coding: utf-8 -*-

import pytest


# the server must be running for this test
def test_client_shorter_than_buffer(capfd):
    from client import client
    client("test_string")
    out, err = capfd.readouterr()
    assert "HTTP/1.1 200 OK" in out