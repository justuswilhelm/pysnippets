from bisect import bisect_left
from math import ceil


class PrimeStore:
    max = 0
    primes = []

    def is_prime(self, n):
        """Bisect the list of primes, since it's sorted."""
        self.calc_primes(n + 1)
        i = bisect_left(self.primes, n)
        if i != len(self.primes) and self.primes[i] == n:
            return True
        else:
            return False

    def calc_primes(self, max):
        if max <= self.max:
            return

        is_prime = [True] * max
        is_prime[0] = False
        is_prime[1] = False

        for i in range(3, int(max ** 0.5) + 1, 2):
            if is_prime[i]:
                for j in range(2, ceil(max / i)):
                    is_prime[i * j] = False

        self.primes = list(map(
            lambda x: x[0], filter(lambda x: x[1], enumerate(is_prime))))

        self.max = self.primes[-1]


def main():
    """
    >>> p = PrimeStore()
    >>> p.is_prime(3)
    True
    >>> p.is_prime(99)
    False
    >>> p.is_prime(9)
    False
    """
    from cProfile import Profile
    from pstats import Stats
    from random import randint
    p = PrimeStore()

    pr = Profile()
    pr.enable()

    for i in [randint(0, 10000) for _ in range(1000)]:
        p.is_prime(i)

    pr.disable()
    stats = Stats(pr)
    assert stats.total_tt < 0.100

if __name__ == "__main__":
    main()
