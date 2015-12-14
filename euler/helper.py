from binascii import hexlify
import hashlib


def md5(solution):
    m = hashlib.md5()
    m.update(str(solution).encode())
    return hexlify(m.digest()).decode()
