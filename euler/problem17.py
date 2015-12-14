import logging
logging.basicConfig(level=logging.INFO)


spell_dict = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    'tens': 'teen',
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60:
    'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
    100: 'one hundred',
    1000: 'one thousand',
}


def spell(number):
    """
    >>> spell(21)
    'twenty-one'
    >>> spell(99)
    'ninety-nine'
    >>> spell(100)
    'one hundred'
    >>> spell(199)
    'one hundred and ninety-nine'
    >>> spell(342)
    'three hundred and forty-two'
    >>> spell(999)
    'nine hundred and ninety-nine'
    >>> spell(1000)
    'one thousand'
    """
    if number < 21:
        return spell_dict[number]
    elif number < 100:
        tens = (number // 10) * 10
        ones = number % 10
        if ones:
            return "{}-{}".format(spell_dict[tens], spell_dict[ones])
        else:
            return spell_dict[tens]
    elif number in [100, 1000]:
        return spell_dict[number]
    elif number < 1000:
        hundreds = (number // 100)
        tens = number // 10 % 10 * 10
        ones = number % 10
        rest = " and " + spell(number % 100) if tens or ones else ""
        return "{} hundred{}".format(spell_dict[hundreds], rest)


def problem17(up_to=1000):
    """
    >>> problem17(5)
    19
    >>> from helper import md5
    >>> md5(problem17())
    '6a979d4a9cf85135408529edc8a133d0'
    """
    result = 0
    for i in range(1, up_to + 1):
        # NOTE: Do not count spaces or hyphens.
        result += len(spell(i).replace(" ", "").replace("-", ""))
    return result
