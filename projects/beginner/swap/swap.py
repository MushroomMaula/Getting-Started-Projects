def swap(a, b):
    """
    Swaps the values of a and b inplace.

    >>> a = [6]  # We use lists as pass by reference only works with mutable objects in python
    >>> b = [3]
    >>> swap(a, b)
    >>> b
    [3]
    >>> a
    [6]

    """
    a, b = b, a


if __name__ == "__main__":
    import doctest
    doctest.testmod()