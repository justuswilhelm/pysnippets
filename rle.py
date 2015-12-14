from sys import argv


def rlencode(data):
    r"""
    >>> from random import randint
    >>> rlencode(bytes([1, 2, 2, 2]) + bytes([1] * 256))
    b'\x01\x01\x03\x02\xff\x01\x01\x01'
    >>> rlencode(bytes([0, 0, 3]))
    b'\x02\x00\x01\x03'
    """
    def pack():
        nonlocal data
        data = list(data)
        prev = None
        count = 0
        for byte in data:
            if byte is not prev or count > 254:
                if prev is not None:
                    yield (prev, count)
                count = 1
                prev = byte
            else:
                count += 1
            prev = byte
        else:
            yield (prev, count)
    result = bytearray()
    for value, count in pack():
        result.append(count)
        result.append(value)
    return bytes(result)


def rldecode(data):
    r"""
    >>> rldecode(b'\x01\xff\xff\x01') == bytes(b'\xff' + 255 * b'\x01')
    True
    """
    result = bytearray()
    for count, value in zip(data[::2], data[1::2]):
        for _ in range(count):
            result.append(value)
    return bytes(result)


if __name__ == "__main__":
    with open(argv[1], 'rb') as fd:
        data = fd.read()
        encoded_data = rlencode(data)
        assert rldecode(encoded_data) == data
        print("Unencoded bytes: {}, RL encoded bytes: {}".format(
            len(data), len(encoded_data)
        ))
        if len(data) < len(encoded_data):
            print("RLE is not suitable for this data.")
        else:
            print("RLE is suited for encoding this kind of data.")
