from sys import exit
from re import compile
__version__ = "10"
if __name__ == "__main__":
    print("Regex Bro version {}".format(__version__))
    inp = input("Input: ")
    regex = compile(input("Regular Expression: "))

    res = list(regex.finditer(inp))
    if not res:
        print("No match")
        exit(1)

    for m in res:
        print("Match: {} at {}".format(
            str(m.group(0)), m.start()))
        for g in m.groups():
            print("Match group {}".format(g))
