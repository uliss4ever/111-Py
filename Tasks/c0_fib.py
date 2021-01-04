def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n <= 2:
        return 1
    n = fib_recursive(n-1) + fib_recursive(n-2)
    print(n)
    return 0


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
def fibb(n):
    fib = [0] * (n+2)
    fib[1] = 1
    for i in range(1, n):
         fib[i+1] += fib[i]
         fib[i+2] += fib[i]
    print(fib[i])
    return 0
fibb(8)