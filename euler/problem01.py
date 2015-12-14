def problem01():
    """
    >>> from helper import md5
    >>> md5(problem01())
    'e1edf9d1967ca96767dcc2b2d6df69f4'
    """
    return sum(i for i in range(1, 1000) if (i % 3 == 0 or i % 5 == 0))
