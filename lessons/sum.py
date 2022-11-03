"""Example of writing a test object."""


from typing import List


def sum(xs: list[float]):
    """Compute the sum of a list."""#type cn + enter to start a new line
    total = 0.0
    i = 0
    while i < len(xs):
        total += xs[i]
        i += 1
    return total

print(sum([1.0,2,0]))