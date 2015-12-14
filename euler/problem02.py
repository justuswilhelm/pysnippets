def problem02():
    """
    >>> from helper import md5
    >>> md5(problem02())
    '4194eb91842c8e7e6df099ca73c38f28'
    """
    def get_fibs(limit=4000000):
        a = 1
        b = 2
        while a < limit:
            yield a
            a, b = b, a + b
        yield b

    result = sum(
        filter(lambda x: not x % 2, get_fibs()))
    return result
