def problem06(n=100):
    """
    >>> problem06(10)
    2640
    >>> from helper import md5
    >>> problem06()
    25164150
    >>> md5(_)
    '867380888952c39a131fe1d832246ecc'
    """
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    square_of_sum = (n ** 4 + 2 * n ** 3 + n ** 2) // 4
    return square_of_sum - sum_of_squares
