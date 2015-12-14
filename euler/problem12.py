import logging
from itertools import count

logging.basicConfig(level=logging.INFO)


def no_divisors(number):
    """
    >>> no_divisors(2)
    2
    >>> no_divisors(5)
    2
    >>> no_divisors(9)
    3
    >>> no_divisors(28)
    6
    >>> no_divisors(140)
    12
    """
    def generate():
        divisors = []
        for i in range(1, int(number ** 0.5) + 1):
            if not number % i:
                yield i
                div = number // i
                if i != div:
                    divisors.append(div)
        for div in divisors:
            yield div
    return len(list(generate()))


def triangle(n):
    # divisors(triangle(n)) == divisors(n) + 1 - 1 ?
    # divisors(a * b) = divisors(a) * divisors(b)
    # n * (n + 1) / 2 == n // 2 * (n + 1) // 2
    return (n * (n + 1)) // 2
    #       a    + 1      - 1

def problem12(min_divisors=500):
    """
    >>> problem12(5)
    28
    >>> from helper import md5
    >>> md5(problem12())
    '8091de7d285989bbfa9a2f9f3bdcc7c0'
    """
    for tr in map(triangle, count(1)):
        divisors = no_divisors(tr)
        if divisors > min_divisors:
            return tr
