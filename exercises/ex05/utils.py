"""Starting ex05."""
__author__ = "730521912"


def only_evens(input: list[int]) -> list[int]:
    """Removing the odd numbers in the list."""
    result: list[int] = list()
    for i in range(len(input)):
        if input[i] % 2 == 0:
            result.append(input[i]) 
    return result


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Combining two list of integers."""
    result: list[int] = list()
    for num1 in list1:
        result.append(num1)
    for num2 in list2:
        result.append(num2)
    return result


def sub(xs: list[int], start_ix: int, end_ix: int) -> list[int]:
    """Return a list which is a subset of the given list, between the start index and the end index - 1."""
    result: list[int] = list()
    if start_ix >= 0 and end_ix < len(xs):
        for i in range(start_ix, end_ix):
            result.append(list[i])
    elif start_ix < 0 & end_ix < len(xs):
        for i in range(0, end_ix):
            result.append(list[i])
    elif start_ix < 0 and end_ix >= len(xs):
        for i in range(0, len(xs)):
            result.append(list[i])
    elif start_ix >= 0 and end_ix >= len(xs):
        for i in range(start_ix, len(xs)):  
            result.append(list[i])        
    return result



    
