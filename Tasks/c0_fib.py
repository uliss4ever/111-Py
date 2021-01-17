def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm
    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    elif n < 1:
        return 0
    elif n <= 2:
        return 1
    fib = fib_recursive(n-1) + fib_recursive(n-2)
    return fib
print(fib_recursive(2))


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm
    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    fib = [0] * (n + 2)
    fib[1] = 1
    for i in range(1, n):
        fib[i + 1] += fib[i]
        fib[i + 2] += fib[i]
    return fib[-2]

if __name__ == "__main__":
    print(fib_iterative(0))

