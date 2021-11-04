from doctest import DocTest


def switch(s: str):
    """
    Switches the case of the string

    >>> switch("Example String!")
    'eXAMPLE sTRING!'
    """
    return s.swapcase()


if __name__ == "__main__":
    import doctest
    doctest.testmod()