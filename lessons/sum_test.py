"""Tests for the sum function."""


from lessons.sum import sum


def test_sum_empty():
    xs = []
    assert sum(xs) == 0.0


def test_single_item():
    xs = [110.0]
    assert sum(xs) == 110.0


def test_sum_many_items():
    xs = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0