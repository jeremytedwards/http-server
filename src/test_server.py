# -*- coding: utf-8 -*-

import pytest


def test_client_shorter_than_buffer(capfd):
    from client import client
    test_string = 'This message is shorter than our buffer'
    client(test_string)
    out, err = capfd.readouterr()
    response = "This message is shorter than our buffer\n"
    assert out == response
