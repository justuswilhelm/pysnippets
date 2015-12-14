from math import ceil


def get_primes(up_to):
    """
    >>> get_primes(10)
    (2, 3, 5, 7)
    """
    is_prime = [True] * up_to
    is_prime[0] = False
    is_prime[1] = False

    for i, isprime in enumerate(is_prime):
        if i in [0, 1]:
            continue
        if not is_prime:
            continue
        for j in range(i ** 2, up_to, i):
            is_prime[j] = False

    primes = tuple(map(
        lambda x: x[0], filter(lambda x: x[1], enumerate(is_prime))))
    return primes


def problem10(below=2000000):
    """
    >>> from helper import md5
    >>> problem10(10)
    17
    >>> md5(problem10())
    'd915b2a9ac8749a6b837404815f1ae25'
    """
    return sum(get_primes(below))
