# -*- coding: utf-8 -*-

import pytest

MSG_TABLE = [
    (u'This message is longer', u'This message is longer\n'),
    (u'shorter', u'shorter\n'),
    (u'exactlen', u'exactlen\n'),
    (u'üñ cool', u'üñ cool\n')
]


@pytest.mark.parametrize('test_string, response', MSG_TABLE)
def test_client_shorter_than_buffer(test_string, response, capfd):
    from client import client
    client(test_string)
    out, err = capfd.readouterr()
    assert out == response
