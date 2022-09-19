""" List Utility Functions."""
__author__ = "730521912"

# def all(int_list: list[int], single_int: int) -> bool:
#     '''Return if the all the elements in int_list is the same as single_int.'''
#     i = 0
#     if len(int_list) == 0:
#         return False
#     while i < len(int_list):
#         if int_list[i] != single_int:
#             return False
#         i += 1
#     return True

def max(input: list[int]) -> int:
    '''Return the largest int in the input list.'''
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i = 1
    max_value = input[0]
    while i < len(input):
        if input[i] > max_value:
            max_value = input[i]
            i = i + 1
            print(i)
    return max_value


print(max([1]))

# def is_equal(list1: list[int], list2: list[int]) -> bool:
#     """Return if two input lists are deeply equal to one another"""
#     i = 0
#     if len(list1) != len(list2):
#         return False
#     while i < len(list1):
#         if list1[i] != list2[i]:
#             return False
#         i += 1
#     return True


