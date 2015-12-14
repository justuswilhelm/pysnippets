from binascii import crc32
from random import shuffle


def insert(element):
    for fn in hash_functions:
        bloom[fn(element)] = True


def test(element):
    return all(bloom[fn(element)] for fn in hash_functions)

if __name__ == "__main__":
    m = 2 ** 20
    hash_functions = [
        lambda x: hash(x) % m,
        lambda x: crc32(str(x)) % m,
    ]
    bloom = [False] * m

    number_test_values = 10000
    test_values = range(number_test_values)
    shuffle(test_values)

    for i in test_values[:-10]:
        insert(i)
        assert test(i)

    for j in test_values[-10:]:
        assert not test(j)
