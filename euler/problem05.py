from functools import lru_cache


@lru_cache()
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


@lru_cache()
def lcm(a, b):
    return (a * b) // gcd(a, b)


@lru_cache()
def problem05(max_divisor=20):
    """
    >>> problem05(10)
    2520
    >>> from helper import md5
    >>> md5(problem05())
    'bc0d0a22a7a46212135ed0ba77d22f3a'
    """
    if max_divisor == 1:
        return 1
    else:
        return lcm(problem05(max_divisor - 1), max_divisor)
