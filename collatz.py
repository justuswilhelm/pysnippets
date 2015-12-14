from functools import lru_cache
from os import getenv

lru_cache_size = int(getenv('CACHE_SIZE', 2**20))


@lru_cache(maxsize=lru_cache_size)
def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return collatz(n // 2)
    else:
        return collatz(3 * n + 1)

if __name__ == "__main__":
    [collatz(n) for n in range(1, 10000)]
