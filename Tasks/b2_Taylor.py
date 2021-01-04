"""
Taylor series
"""
from typing import Union


def fact():
    a = 1
    x = 1
    while a >= 0:
        x *= a
        yield x
        a += 1
g = fact()
#
#
# def ex(x: Union[int, float]) -> float:
#     """ Calculate value of e^x with Taylor series
#     :param x: x value
#     :return: e^x value
#     """
#     n = 50
#     res = 1
#     val = fact()
#     for a in range(1, n):
#         res += x**a/next(val)
#     return round(res, 5)
#     # return 0
# print(ex(5.5))


def sinx(x: Union[int, float]) -> float:

    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    n = 50
    res = x
    val = fact()
    next(val)
    for a in range(1, n):
        next(val)
        res += ((-1)**a) * (x ** (2*a+1)) / (next(val))

    return round(res, 5)


print(sinx(3.1416/2*3))
