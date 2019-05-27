import pytest

from .helpers import example, example2, example3


def test_example_py():
    assert example() == True

def test_example2_py():
    assert example2() == True

def test_example3_py():
    assert example3() == True
