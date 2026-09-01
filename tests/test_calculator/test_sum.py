from pytest import raises
from calculator.sum import sum


def test_sum():
    assert sum(5, 6) == 11


def test_sum_2():
    assert sum(6, 7) == 13


# def test_exception():
#     with raises(Exception):
#         sum(1, 1)
