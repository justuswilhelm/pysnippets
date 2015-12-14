from collections import defaultdict
from io import StringIO
from re import compile

WORD_RE = compile(r"[\w']+")


def find_and_print(word):
    print("Looking for '{}'...".format(word))
    text.seek(0)
    lines = text.readlines()
    for file_name, line, column in index[word]:
        print("{}@{},{}: {}".format(
            file_name,
            line,
            column,
            lines[line].strip().replace(word, ">{}<".format(word))
        ))


if __name__ == "__main__":
    text = StringIO("""
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    """)
    index = defaultdict(list)
    for line_no, line in enumerate(text.readlines()):
        for match in WORD_RE.finditer(line):
            column = match.start()
            word = match.group(0).lower()
            index[word].append(("import this", line_no, column))
    while True:
        query = input('> ')
        find_and_print(query)
