def primes(n: int):
    """
    Returns a list containing all prime numbers less or equal n
    
    >>> primes(5)
    [2, 3, 5]
    """
    # Generate a array containing all numbers up to n
    # Can be optimized by just going up to sqrt(n)
    nums = list(range(2, n+1))
    primes = []
    for n in nums:
        is_prime = True
        for p in primes:
            if n % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(n)

    return primes


if __name__ == "__main__":
    import doctest
    doctest.testmod()