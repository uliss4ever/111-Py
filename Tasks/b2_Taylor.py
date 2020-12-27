"""
Taylor series
"""
from typing import Union


def fact(x: int) -> int:
    a = 1
    x = 1
    while a >= 0:
        x *= a
        yield x
        a += 1


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    n = 50
    res = 1
    val = fact(0)
    for a in range(1, n):
        res += x**a/next(val)
        # print(res)

    return round(res, 5)
    # return 0
print(ex(5.5))


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    print(x)
    return 0
