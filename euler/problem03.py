from math import ceil


def primes(max):
    """
    >>> list(primes(4))
    [2, 3]
    """
    is_prime = [True] * max
    for i in range(3, int(max ** 0.5) + 1, 2):
        if is_prime[i]:
            for j in range(2, ceil(max / i)):
                is_prime[i * j] = False

    for no, i in enumerate(is_prime):
        if i and no > 1:
            yield no


def prime_factors(number):
    """
    >>> list(prime_factors(27))
    [3]
    """
    for i in primes(int(number ** 0.5) + 1):
        if not number % i:
            yield i


def problem03(number=600851475143):
    """
    >>> problem03(13195)
    29
    >>> from helper import md5
    >>> md5(problem03())
    '94c4dd41f9dddce696557d3717d98d82'
    """
    return max(prime_factors(number))
