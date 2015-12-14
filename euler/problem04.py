def problem04(digits=3):
    """
    >>> problem04(2)
    9009
    >>> from helper import md5
    >>> problem04()
    906609
    >>> md5(_)
    'd4cfc27d16ea72a96b83d9bdef6ce2ec'
    """
    def get_products(min, max):
        for i in range(min_factor, max_factor):
            for j in range(i, max_factor):
                yield i * j

    is_palindrome = lambda nr: str(nr) == str(nr)[::-1]
    min_factor = int("9" + "0" * (digits - 1))
    max_factor = int("9" * digits) + 1
    return max(filter(
        is_palindrome, get_products(min_factor, max_factor)))
