"""
Taylor series
"""
from typing import Union

def step(x):
    t = 1
    while True:
        t *= x
        yield t


def fact():
    a = 1
    x = 1
    while a >= 0:
        x *= a
        yield x
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
    val1 = step(x)
    for a in range(1, n):
        res += next(val1)/next(val)
    return round(res, 5)

print(ex(5.5))


def step_for_sin(x):
    a = 1
    d = 1
    while True:
        a *= x
        if d > 2 and d % 2:
            yield a
        d += 1

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
    k = step_for_sin(x)
    for a in range(1, n):
        res += ((-1)**a) * (next(k)) / (next(g))
    return round(res, 5)


print(sinx(3.1416/2*3))
