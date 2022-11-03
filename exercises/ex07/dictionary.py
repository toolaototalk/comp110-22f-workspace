"""EX01 - Dictionary."""

__author__ = "730521912"
from collections import Counter


def invert(og: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values from input dict."""
    result: dict[str, str] = {}
    counter = Counter(og.values())
    if counter.most_common(1)[0][1] >= 2:
        raise KeyError
    for key in og:
        result[og[key]] = key
    return result


def favorite_color(dict1: dict[str, str]) -> str:
    """Returns a str which is the color that appears most frequently."""
    counter = Counter(dict1.values())
    result = counter.most_common(1)[0][0]
    return result


def count(list1: list[str]) -> dict[str, int]:
    """Return a dictionary of the counts of each of the items in the input list."""
    result: dict[str, int] = {}
    for i in list1:
        if i in result.keys():
            result[i] += 1
        else:
            result[i] = 1
    # for item in list1:
    #     if item in result:
    #         pass
    #     result[item] = list1.count(item)
    return result
