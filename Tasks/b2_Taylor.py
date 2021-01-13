"""
Taylor series
"""
from typing import Union

def step(x):
    a = 1
    while True:
        x **= a
        yield x
        a += 1

s = step(2)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))


def fact():
    a = 1
    t = 1
    while True:
        t *= a
        yield t
        a += 1
g = fact()


def ex(x: Union[int, float]) -> float:
    """ Calculate value of e^x with Taylor series
    :param x: x value
    :return: e^x value
    """
    n = 50
    res = 1
    val = fact()
    for a in range(1, n):
        res += x**a/next(val)
    return round(res, 5)

# print(ex(5.5))

def fact_for_sin():
    a = 1
    x = 1
    while True:
        x *= a
        if a > 2 and a % 2:
            yield x
        a += 1
g = fact_for_sin()


def sinx(x: Union[int, float]) -> float:

    n = 50
    res = x
    g = fact_for_sin()
    for a in range(1, n):
        res += ((-1)**a) * (x ** (2*a+1)) / (next(g))
    return round(res, 5)


# print(sinx(3.1416/2*3))
