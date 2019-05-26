import pytest

from .helpers import example, example2


def test_example_py():
    assert example() == True

def test_example2_py():
    assert example2() == True
