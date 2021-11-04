def natural_sqrt(n: int):
    """
    Return the last number that is squared less than n.

    >>> natural_sqrt(9)
    3
    >>> natural_sqrt(5)
    2
    """
    if n < 1:
        raise ValueError("n must be a greater than zero.")

    i = 1
    while i*i <= n:
        i += 1

    return i-1


if __name__ == "__main__":
    import doctest
    doctest.testmod()