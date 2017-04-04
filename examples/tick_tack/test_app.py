from app import add

import pytest


def add_data():
    for x in xrange(0, 100):
        for y in xrange(0, 100):
            yield x, y


@pytest.mark.parametrize('x, y', add_data())
def test_app_simple(x, y):
    actual = add(x, y)
    assert actual['result'] == str(x + y)
