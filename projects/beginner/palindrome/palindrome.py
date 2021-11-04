def palindrome(s: str):
    """
    Checks whether s is a palindrome

    >>> palindrome("anna")
    True
    >>> palindrome("abc")
    False
    """
    return s == s[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()