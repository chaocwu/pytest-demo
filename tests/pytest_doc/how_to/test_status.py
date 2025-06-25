from random import randint
import pytest


def test_passed():
    assert True


def test_failed():
    assert False


@pytest.mark.skip(reason="This test is skipped")
def test_skipped():
    assert True


def test_broken():
    raise Exception("This test is broken")


@pytest.mark.parametrize("value", [randint(2, 4) for _ in range(2)])
def test_parametrized(value):
    assert value % 2 == 0, f"Value {value} is not even"
