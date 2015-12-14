from functools import lru_cache

@lru_cache(maxsize=2**20)
def collatz_chain_length(n):
    """
    >>> collatz_chain_length(13)
    10
    >>> collatz_chain_length(102)
    26
    """
    if n == 1:
        return 1
    if not n % 2:
        return 1+ collatz_chain_length(n // 2)
    else:
        return 1 + collatz_chain_length(3 * n + 1)


def problem14():
    """
    >>> from helper import md5
    >>> md5(problem14())
    '5052c3765262bb2c6be537abd60b305e'
    """
    longest_chain = 0
    longest_chain_no = 0
    for i in range(1, 1000000):
        ch = collatz_chain_length(i)
        if ch > longest_chain:
            longest_chain = ch
            longest_chain_no = i
    return longest_chain_no
