def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n <= 0:
        raise ValueError
    elif n == 1:
        return 1
    ft = n * factorial_recursive(n - 1)
    return ft

print(factorial_recursive(2))


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way
    :param n: int > 0
    :return: factorial of n
    """
    if n <= 0:
        raise ValueError
    ft = n
    for i in range(1, n):
        ft *=i
        print(ft)
    return ft
factorial_iterative(5)