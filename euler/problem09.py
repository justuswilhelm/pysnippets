def is_pythagorean_triplet(a, b, c):
    """
    >>> is_pythagorean_triplet(3, 4, 5)
    True
    >>> is_pythagorean_triplet(4, 4, 9)
    False
    """
    return (a ** 2 + b ** 2) == c ** 2 and a < b < c


def problem09():
    """
    >>> from helper import md5
    >>> md5(problem09())
    '24eaa9820350012ff678de47cb85b639'
    """
    for a in range(1000):
        for b in range(1000):
            for c in range(1000):
                if a + b + c == 1000 and is_pythagorean_triplet(
                        a, b, c):
                    return a * b *c
