"""Ex05 test file."""
__author__ = "730521912"
from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:
    """Testing empty list input."""
    xs1: list[int] = []
    assert only_evens(xs1) == []


def test_only_evens_all_odd() -> None:
    """Testing input list of only odd numbers."""
    xs2: list[int] = [1, 3, 5]
    assert only_evens(xs2) == []


def test_only_evens_mixed() -> None:
    """Testing input list of both odd and even numbers."""
    xs3: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs3) == [2, 4, 6]


def test_concat_empty() -> None:
    """Testing adding two empty list."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []


def test_concat_no_modifying() -> None:
    """Testing if concat function will modify the input list."""
    list1: list[int] = [1, 2]
    list2: list[int] = [3, 4]
    concat(list1, list2)
    assert list1 == list1 and list2 == list2


def test_concat_use() -> None:
    """Testing use case of concat()."""
    list1: list[int] = [1, 2]
    list2: list[int] = [3, 4]
    assert concat(list1, list2) == [1, 2, 3, 4]


def test_sub_negative_start() -> None:
    """Testing sub() with negative start index."""
    list: list[int] = [1, 2, 3]
    assert sub(list, -1, 2) == [1, 2]


def test_sub_end_out_of_bound() -> None:
    """Testing sub() with end index greater than length of input list."""
    list: list[int] = [1, 2]
    assert sub(list, 1, 999) == [2]


def test_sub_use() -> None:
    """Testing normal use case of sub()."""
    list: list[int] = [1, 2, 3]
    assert sub(list, 0, 2) == [list[0], list[1]]
    
