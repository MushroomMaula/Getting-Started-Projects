def fibonacci(n: int):
    """
    Returns the nth fibonacci number

    >>> fibonacci(5)
    5
    """
    if n < 2:
        return n

    # The third fibonacci number
    previous = 1  # Fib(n-2)
    num = 2  # Fib(n-1)
    for i in range(3, n):
        tmp = num  # Save fib(n-1)
        num += previous
        previous = tmp

    return num


if __name__ == "__main__":
    import doctest
    doctest.testmod()