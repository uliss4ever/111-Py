"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    if not arr:
        return -1

    min_ind = 0
    min = arr[min_ind]
    for index in range(len(arr)):
        if arr[index] < min:
            min = arr[index]
            min_ind = index
    return min_ind

