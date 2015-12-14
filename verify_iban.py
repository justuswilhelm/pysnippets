#!/usr/bin/env python3
"""Verify a given IBAN number."""
from string import ascii_lowercase

LETTER_MAPPING = {
    a: i + 10 for a, i in zip(
        ascii_lowercase,
        range(len(ascii_lowercase)))
}

prepare = lambda iban: iban.replace(" ", "")
swap_iban = lambda iban: iban[4:] + iban[:4]
replace_letters = lambda iban: "".join(
    [str(LETTER_MAPPING[e]) if e in ascii_lowercase
     else e for e in iban.lower()])


def verify(iban):
    """
    >>> verify("DE89 3704 0044 0532 0130 00")
    True
    >>> verify("DE89 3704 0044 0532 0130 01")
    False
    """
    prepared_iban = int(replace_letters(swap_iban(prepare(iban))))
    result = prepared_iban % 97 == 1
    return result

if __name__ == "__main__":
    iban = input("IBAN> ")
    assert verify(iban), "Checksum Error"
