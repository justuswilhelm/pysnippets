def problem16(n=1000):
    """
    >>> from helper import md5
    >>> problem16(n=15)
    26
    >>> md5(problem16(1000))
    '6a5889bb0190d0211a991f47bb19a777'
    """
    digits = [int(d) for d in str(2 ** n)]
    return sum(digits)
