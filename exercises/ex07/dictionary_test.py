"""Unit tests for dictionary functions."""
__author__ = "730521912"

from dictionary import invert, favorite_color, count
import pytest


def test_invert() -> None:
    """Edge Case Test for the invert function."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_invert_1() -> None:
    """Edge Case Test for the invert function."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_2() -> None:
    """Second Use Case Test for the invert function."""
    xs: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_favorite_color() -> None:
    """Edge Case Test for the favorite colors function."""
    xs: dict[str, str] = {"a": "red"}
    assert favorite_color(xs) == "red"


def test_favorite_color_1() -> None:
    """First Use Case Test for the favorite colors function."""
    xs: dict[str, str] = {"a": "red", "b": "red", "c": "blue", "d": "black"}
    assert favorite_color(xs) == "red"


def test_favorite_color_2() -> None:
    """Second Use Case Test for the favorite colors function."""
    xs: dict[str, str] = {"a": "red", "b": "red", "c": "red", "d": "black"}
    assert favorite_color(xs) == "red"


def test_count() -> None:
    """Edge Case Test for the count function."""
    xs: list = ["a"]
    assert count(xs) == {"a": 1}


def test_count_1() -> None:
    """First Use Case Test for the count function."""
    xs: list = ["a", "a", "b"]
    assert count(xs) == {"a": 2, "b": 1}


def test_count_2() -> None:
    """Second Use Case Test for the count function."""
    xs: list = ["a", "a", "a", "c", "c", "b"]
    assert count(xs) == {'a': 3, 'c': 2, 'b': 1}
