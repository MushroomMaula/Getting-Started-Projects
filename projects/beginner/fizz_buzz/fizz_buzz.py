def fizz_buzz(n: int):
    """
    >>> fizz_buzz(6)
    1
    2
    Fizz
    4
    Buzz
    Fizz

    """
    for i in range(1, n+1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    import doctest
    doctest.testmod()