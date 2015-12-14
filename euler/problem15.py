from functools import lru_cache
from cProfile import Profile
from pstats import Stats


import logging
logging.basicConfig(level=logging.INFO)

@lru_cache(maxsize=None)
def factor(n):
    """
    >>> factor(1)
    1
    >>> factor(2)
    2
    >>> factor(3)
    6
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factor(n - 1)


def binom(n, k):
    """
    >>> binom(10, 0)
    1
    >>> binom(10, 1)
    10
    >>> binom(10, 10)
    1
    """
    if n == k or k == 0:
        return 1

    return (factor(n)) // (factor(k) * factor(n - k))


def lattice_paths(grid_size=20):
    """
    >>> from helper import md5
    >>> lattice_paths(1)
    2
    >>> lattice_paths(2)
    6
    >>> md5(lattice_paths())
    '928f3957168ac592c4215dcd04e0b678'
    """
    path_length = grid_size * 2
    return binom(path_length, grid_size)



if __name__ == "__main__":
    p = Profile()
    p.enable()
    lattice_paths(10)
    p.disable()
    ps = Stats(p).sort_stats('cumulative')
    ps.print_stats()
