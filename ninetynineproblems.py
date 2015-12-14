"""
http://www.ic.unicamp.br/~meidanis/courses/mc336/2009s2/prolog/problemas/index.html

Problems not solved:
- Problem 27
- Problem 55
- Problem 58
- Problem 59
- Problem 60
- Problem 63
- Problem 65
- Problem 66
"""
from collections import Counter
from functools import lru_cache
from random import randint

a, b, c, d, e, f, g, h = range(8)
t = lambda a, b, c=None: (a, b) if not c else (a, b, c)


def last(lst):
    """
    Problem 01

    >>> last([1, 2, 3, 4])
    4
    """
    return lst[-1]


def second_last(lst):
    """
    Problem 02

    >>> second_last([1, 2, 3, 4])
    3
    """
    return lst[-2]


def element_at(lst, index):
    """
    Problem 03

    >>> element_at([1, 2, 3, 4], 2)
    3
    """
    head, *tail = lst
    if not index:
        return head
    else:
        return element_at(tail, index - 1)


def length(lst):
    """
    Problem 04

    >>> length([1, 2, 3, 4])
    4
    """
    _, *tail = lst
    if tail:
        return 1 + length(tail)
    else:
        return 1


def reverse(lst):
    """
    Problem 05

    >>> list(reverse([1, 2, 3, 4]))
    [4, 3, 2, 1]
    """
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]


def is_palindrome(lst):
    """
    Problem 06

    >>> is_palindrome([2, 3, 1, 3, 2])
    True
    >>> is_palindrome([2, 3, 3, 2])
    True
    """
    for a, b in zip(reverse(lst), lst):
        if a != b:
            return False
    return True


def flatten(lst):
    """
    Problem 07

    >>> flatten([1, [2, [3, 4], 5]])
    [1, 2, 3, 4, 5]
    >>> flatten((1, (2, (3, 4), 5)))
    [1, 2, 3, 4, 5]
    """
    if lst:
        head, *tail = lst
        if type(head) not in [list, tuple]:
            return [head] + flatten(tail)
        else:
            return flatten(head) + flatten(tail)
    else:
        return []


def compress(lst):
    """
    Problem 08

    >>> list(compress([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]))
    [1, 2, 3, 1, 4, 5]
    """
    for prev, cur in zip([None] + lst[:-1], lst):
        if prev is not cur:
            yield cur


def pack(lst):
    """
    Problem 09

    >>> list(pack([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]))
    [[1, 1, 1, 1], [2], [3, 3], [1, 1], [4], [5, 5, 5, 5]]
    """
    from itertools import groupby
    return (list(l[1]) for l in groupby(lst))


def encode(lst):
    """
    Problem 10

    >>> list(encode([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]))
    [[4, 1], [1, 2], [2, 3], [2, 1], [1, 4], [4, 5]]
    """
    for l in pack(lst):
        yield [l.count(l[0]), l[0]]


def encode_modified(lst):
    """
    Problem 11

    >>> list(encode_modified([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]))
    [[4, 1], 2, [2, 3], [2, 1], 4, [4, 5]]
    """
    for l in encode(lst):
        yield l[1] if l[0] == 1 else l


def decode(lst):
    """
    Problem 12

    >>> list(decode([[4, 1], 2, [2, 3], [2, 1], 4, [4, 5]]))
    [1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]
    """
    def aux():
        for e in lst:
            yield [1, e] if type(e) is not list else e
    return flatten_once([elt] * occ for (occ, elt) in aux())


def flatten_once(lst):
    return (inner for outer in lst for inner in outer)


def encode_direct(lst):
    """
    Problem 13
    >>> encode_direct(None)
    """


def dupli(lst):
    """
    Problem 14

    >>> list(dupli([1, 2, 3]))
    [1, 1, 2, 2, 3, 3]
    """
    return flatten_once([e] * 2 for e in lst)


def dupli_times(lst, times):
    """
    Problem 15

    >>> list(dupli_times([1, 2, 3], 3))
    [1, 1, 1, 2, 2, 2, 3, 3, 3]

    """
    return flatten_once([e] * times for e in lst)


def drop(lst, n):
    """
    Problem 16

    >>> list(drop([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    [1, 2, 4, 5, 7, 8]
    """
    for index, a in enumerate(lst):
        if (index + 1) % n:
            yield a


def split(lst, index):
    """
    Problem 17

    >>> split([1, 2, 3], 1)
    ([1, 2], [3])
    """
    return lst[:index+1], lst[index+1:]


def slice(lst, i, k):
    """
    Problem 18

    >>> slice([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7)
    [3, 4, 5, 6, 7]
    """
    _, *tail = lst
    return slice(tail, i - 1, k - 1) if i > 1 else split(lst, k - 1)[0]


def rotate(lst, i):
    """
    Problem 19

    >>> rotate([1, 2, 3, 4, 5, 6, 7, 8], 3)
    [4, 5, 6, 7, 8, 1, 2, 3]
    >>> rotate([1, 2, 3, 4, 5, 6, 7, 8], -2)
    [7, 8, 1, 2, 3, 4, 5, 6]
    """
    if not i:
        return lst
    else:
        if i > 0:
            return rotate(lst[1:] + lst[:1], i - 1)
        else:
            return rotate(lst[-1:] + lst[:-1], i + 1)


def remove_at(lst, k):
    """
    Problem 20

    This is like taking candy from a child
    >>> remove_at([1, 2, 3], 2)
    [1, 2]
    """
    return lst[:k] + lst[k + 1:]


def insert_at(l, lst, index):
    """
    Problem 21

    >>> insert_at(5, [1, 2, 3], 2)
    [1, 2, 5, 3]
    """
    return lst[:index] + [l] + lst[index:]


def my_range(start, end):
    """
    Problem 22

    >>> list(my_range(4, 9))
    [4, 5, 6, 7, 8, 9]
    """
    while start <= end:
        yield start
        start += 1


def rnd_select(iter, count):
    """
    Problem 23

    >>> len(list(rnd_select([1, 2, 3], 2)))
    2
    >>> list(sorted(rnd_select(range(123), 123))) == list(range(123))
    True
    """
    lst = list(iter)
    chosen = 0
    while chosen < count:
        yield lst.pop(randint(0, len(lst) - 1))
        chosen += 1


def lotto(n, m):
    """
    Problem 24

    >>> len(list(lotto(6, 49)))
    6
    >>> sorted(lotto(49, 49)) == list(range(1, 50))
    True
    """
    return rnd_select(my_range(1, m), n)


def rnd_permu(lst):
    """
    Problem 25

    >>> len(list(rnd_permu([1, 2, 3])))
    3
    """
    return rnd_select(lst, len(lst))


def lsort(lst):
    """
    Problem 28a

    >>> lsort([[1, 2, 3], [4, 5], [6, 7, 8], [4, 5], [9, 10, 11, 12],\
        [13, 14], [15]])
    [[15], [4, 5], [4, 5], [13, 14], [1, 2, 3], [6, 7, 8], [9, 10, 11, 12]]
    """
    return sorted(lst, key=len)


def lfsort(lst):
    """
    Problem 28b

    >>> list(lfsort([[1, 2, 3], [4, 5], [6, 7, 8], [4, 5], [9, 10, 11, 12],\
        [13, 14], [15]]))
    [(4, 5), (15,), (13, 14), (9, 10, 11, 12), (6, 7, 8), (1, 2, 3)]
    """
    for e in Counter(tuple(a) for a in lst).most_common():
        yield e[0]


def is_prime(n):
    """
    Problem 31

    >>> is_prime(23)
    True
    >>> is_prime(4)
    False
    >>> is_prime(3)
    True
    """
    return all(n % i for i in range(2, int(n ** 0.5 + 1)))


def gcd(n, m):
    """
    Problem 32

    >>> gcd(36, 63)
    9
    """
    if not m:
        return n
    else:
        return gcd(m, n % m)


def coprime(n, m):
    """
    Problem 33

    >>> coprime(35, 64)
    True
    """
    return gcd(n, m) == 1


def phi(m):
    """
    Problem 34

    >>> phi(10)
    4
    >>> phi(7)
    6
    """
    result = 0
    for candidate in range(m):
        if coprime(m, candidate):
            result += 1
    return result


def prime_factors(n):
    """
    Problem 35: Determine the prime factors of a given positive integer

    Construct a flat list containing the prime factors in ascending order.
    Example:
    >>> list(prime_factors(315))
    [3, 3, 5, 7]
    """
    for candidate in range(2, int(n ** 0.5) + 1):
        while not n % candidate:
            n = n // candidate
            yield candidate


def prime_factors_mult(n):
    """
    Problem 36: Determine the prime factors of a given positive integer

    Construct a list containing the prime factors and their multiplicity.
    Example:
    >>> list(prime_factors_mult(315))
    [(3, 2), (5, 1), (7, 1)]
    """
    return ((b, a) for a, b in encode(prime_factors(n)))


def phi_improved(n):
    """
    Problem 37

    >>> phi(10)
    4
    >>> phi(7)
    6
    """
    l = prime_factors_mult(n)
    result = 1
    for prime, multiples in l:
        result *= (prime - 1) * prime ** (multiples - 1)


def compare_phi():
    """
    Problem 38
    >>> a, b = compare_phi()
    >>> a > b
    True
    """
    from cProfile import Profile
    from pstats import Stats
    pr_normal = Profile()
    pr_normal.enable()
    phi(10090)
    pr_normal.disable()
    time_normal = Stats(pr_normal).total_tt
    pr_improved = Profile()
    pr_improved.enable()
    phi_improved(10090)
    pr_improved.disable()
    time_improved = Stats(pr_improved).total_tt
    return time_normal, time_improved


def goldbach(n):
    """
    Problem 39

    >>> goldbach(28)
    (5, 23)
    """
    for a in filter(is_prime, range(2, n)):
        for b in filter(is_prime, range(max(a, 2), n)):
            if a + b == n:
                return a, b


def goldbach_list(lower, upper):
    """
    Problem 40

    >>> goldbach_list(9,20)
    10 = 3 + 7
    12 = 5 + 7
    14 = 3 + 11
    16 = 3 + 13
    18 = 5 + 13
    20 = 3 + 17
    """
    for i in range(lower + 1, upper + 1, 2):
        print("{} = {} + {}".format(i, *goldbach(i)))


def table(expr):
    """
    Problem 46

    >>> table("and(A,or(A,B))")
    true true true
    true fail true
    fail true fail
    fail fail fail
    """
    from operator import and_, or_, xor  # noqa
    nand = lambda a, b: not and_(a, b)
    nor = lambda a, b: not or_(a, b)
    equ = lambda a, b: a is b
    impl = lambda a, b: a or not b
    clean_expr = expr.replace('and', 'and_').replace('or', 'or_')
    compiled_expr = compile(clean_expr, '<string>', 'eval')
    for A in [True, False]:
        for B in [True, False]:
            C = eval(compiled_expr)
            print("{A} {B} {C}".format(**locals())
                  .lower().replace('false', 'fail'))


def table_infix(expr):
    """
    Problem 47

    >>> table_infix("A and (A or not B)")
    true true true
    true fail true
    fail true fail
    fail fail fail
    """
    compiled_expr = compile(expr, '<string>', 'eval')
    for A in [True, False]:
        for B in [True, False]:
            C = eval(compiled_expr)
            print("{A} {B} {C}".format(**locals())
                  .lower().replace('false', 'fail'))


def table_general(variables, expr):
    """
    Problem 48

    I cheated here and some of the results are not the same because of the way
    Python handles operator precedence.
    >>> table_general(['A', 'B', 'C'], 'A and (B or C) equ A and B or A and C')
    true true true true
    true true fail true
    true fail true true
    true fail fail fail
    fail true true fail
    fail true fail fail
    fail fail true fail
    fail fail fail fail
    """
    cleaned_expr = expr.replace('equ', '==')
    compiled_expr = compile(cleaned_expr, '<string>', 'eval')

    for i in reversed(range(2 ** len(variables))):
        values = [bool(int(i)) for i in bin(i)[2:].zfill(3)]
        for var, value in zip(variables, values):
            locals()[var] = value
        result = eval(compiled_expr)
        print((" ".join(["{" + var + "}" for var in variables]) + " {result}")
              .format(**locals()).lower().replace('false', 'fail'))


@lru_cache(maxsize=1024)
def gray_code(n):
    """
    Problem 50

    >>> gray_code(1)
    ['0', '1']
    >>> gray_code(2)
    ['00', '01', '11', '10']
    >>> gray_code(3)
    ['000', '001', '011', '010', '110', '111', '101', '100']
    """
    if n == 1:
        return ['0', '1']
    else:
        return ['0' + code for code in gray_code(n - 1)] + [
            '1' + code for code in reversed(gray_code(n - 1))]


def istree(t):
    """
    Problem 54

    I took the liberty of encoding trees as Python tuples.
    >>> istree(None)
    True
    >>> istree((1, (2, None, None), None))
    True
    >>> istree((1, (2, None, None)))
    False
    """
    if t is not None:
        try:
            return istree(t[1]) and istree(t[2])
        except IndexError:
            return False
    else:
        return True


def symmetric(t_a):
    """
    Problem 56

    >>> symmetric((1,\
        (2, None, None),\
        (2, None, None)))
    True
    >>> symmetric((0,\
        (1, (2, None, None), None),\
        (1, None, (2, None, None))))
    True
    >>> symmetric((1,\
        (2, (1, None, None), None),\
        (2, None, (2, None, None))))
    True
    """
    clean = lambda t: (
        0, clean(t[1]), clean(t[2])) if type(t) in (list, tuple) else None
    invert = lambda t: (
        t[0], invert(t[2]), invert(t[1])) if type(t) in (list, tuple) else None
    t_a = clean(t_a)
    try:
        return t_a == invert(t_a)
    except TypeError:
        return False


def append(tree, item, position=0):
    """
    >>> t = [1, [2, None, None], [3, None, None]]
    >>> append(t, 4)
    >>> t
    [1, [2, None, None], [3, None, [4, None, None]]]
    >>> append(t, 5)
    >>> t
    [1, [2, None, None], [3, None, [4, None, [5, None, None]]]]
    """

    if tree[position] > item:
        if tree[position + 1] is None:
            tree[position + 1] = [item, None, None]
        else:
            append(tree[position + 1], item)
    else:
        if tree[position + 2] is None:
            tree[position + 2] = [item, None, None]
        else:
            append(tree[position + 2], item)


def treeify(lst):
    tree = [lst.pop(0), None, None]
    while lst:
        append(tree, lst.pop(0))
    return tree


def construct(lst):
    """
    Problem 57

    >>> a = construct([3, 2, 5, 7, 1])
    >>> a
    [3, [2, [1, None, None], None], [5, None, [7, None, None]]]
    >>> symmetric(a)
    True
    >>> symmetric(construct([5, 3, 18, 1, 4, 12, 21]))
    True
    >>> symmetric(construct([3,2,5,7,4]))
    False
    """

    root = lst[0]
    lesser = sorted(filter(lambda e: e < root, lst), reverse=True)
    higher = sorted(filter(lambda e: e > root, lst))
    return [root, treeify(lesser), treeify(higher)]


def count_leaves(tree):
    """
    Problem 61

    >>> count_leaves(\
        [3, [2, [1, None, None], None], [5, None, [7, None, None]]])
    2
    """
    if tree is None:
        return 0
    if tree[1] is None and tree[2] is None:
        return 1
    else:
        return sum(count_leaves(child) for child in tree[1:])


def leaves(tree):
    """
    Problem 61A

    >>> sorted(leaves(\
        [3, [2, [1, None, None], None], [5, None, [7, None, None]]]))
    [1, 7]
    """
    accumulator = []

    def collect(tree, accumulator=accumulator):
        if tree is None:
            return
        elif tree[1] is None and tree[2] is None:
            accumulator.append(tree[0])
        else:
            collect(tree[1])
            collect(tree[2])

    collect(tree)
    return accumulator


def internals(tree):
    """
    Problem 62

    >>> sorted(internals(\
        [3, [2, [1, None, None], None], [5, None, [7, None, None]]]))
    [2, 3, 5]
    """
    accumulator = []

    def collect(tree, accumulator=accumulator):
        if tree is None:
            return
        elif any(tree[1:]):
            accumulator.append(tree[0])
            collect(tree[1])
            collect(tree[2])

    collect(tree)
    return accumulator


def atlevel(tree, level):
    """
    Problem 62B

    >>> sorted(atlevel(\
        [3, [2, [1, None, None], None], [5, None, [7, None, None]]], 3))
    [1, 7]
    """
    accumulator = []

    def collect(tree, current_level=1, level=level, accumulator=accumulator):
        if level == current_level and tree is not None:
            accumulator.append(tree[0])
        elif tree is not None:
            collect(tree[1], current_level + 1)
            collect(tree[2], current_level + 1)

    collect(tree)
    return accumulator


def layout_binary_tree(tree):
    """
    Problem 64

    >>> layout_binary_tree(\
        [3, [2, [1, None, None], None], [5, None, [7, None, None]]])
    [3, 3, 1, [2, 2, 2, [1, 1, 3, None, None], None], \
[5, 4, 2, None, [7, 5, 3, None, None]]]
    """
    from copy import deepcopy
    tree = deepcopy(tree)

    sequence = {item: position for position, item in enumerate(sorted(
        internals(tree) + leaves(tree)))}

    def decorate(tree, height=1):
        if tree is not None:
            tree.append(tree[1])
            tree.append(tree[2])
            tree[1] = sequence[tree[0]] + 1
            tree[2] = height
            decorate(tree[3], height + 1)
            decorate(tree[4], height + 1)

    decorate(tree)
    return tree


def tree_string(tree):
    """
    Problem 67a

    >>> tree_string(\
        [3, [2, [1, None, None], None], [5, None, [7, None, None]]])
    '3(2(1,),5(,7))'
    """
    from re import sub
    tree = str(tree)
    tree = sub(r"\[(\d),", r"\1(", tree)
    tree = tree.replace("None", "")
    tree = tree.replace("]", ")")
    tree = tree.replace(" ", "")
    tree = tree.replace("(,)", "")
    return tree


def string_tree(string):
    """
    Problem 67b

    >>> string_tree('3(2(1,),5(,7))')
    [3, [2, [1, None, None], None], [5, None, [7, None, None]]]
    >>> string_tree('1(2(4,5),3(,6(7,)))')
    [1, [2, [4, None, None], [5, None, None]], \
[3, None, [6, [7, None, None], None]]]
    """
    def childify(tree):
        if isinstance(tree[1], int):
            tree[1] = [tree[1], None, None]
        elif tree[1] is not None:
            childify(tree[1])
        if isinstance(tree[2], int):
            tree[2] = [tree[2], None, None]
        elif tree[2] is not None:
            childify(tree[2])
    from re import sub
    string = string.replace("(", "[")
    string = string.replace(")", "]")
    string = sub(r"(\d)\[", r"[\1, ", string)
    string = string.replace(", ,", ", None, ")
    string = string.replace(",]", ", None]")
    tree = eval(string)
    childify(tree)
    return tree


def preorder(tree):
    """
    Problem 68a1

    >>> preorder([1, [2, [4, None, None], [5, None, None]],\
        [3, None, [6, None, None]]])
    [1, 2, 3, 4, 5, 6]
    """
    result = []
    goals = [tree]
    while goals:
        current = goals.pop(0)
        result.append(current[0])
        if current[1] is not None:
            goals.append(current[1])
        if current[2] is not None:
            goals.append(current[2])
    return result


def inorder(tree):
    """
    Problem 68a2

    >>> inorder([1, [2, 4, 5], [3, None, [6, None, None]]])
    [1, 2, 4, 5, 3, 6]
    """
    if tree is None:
        return []
    if isinstance(tree, int):
        return [tree]
    if tree[1] is None and tree[2] is None:
        return [tree[0]]
    else:
        return [tree[0]] + inorder(tree[1]) + inorder(tree[2])


def dotstring_tree(dotstring):
    """
    Problem 69a

    >>> dotstring_tree('124..5..3.67...')
    [1, [2, [4, None, None], [5, None, None]], [3, None, [6, [7, None, None], \
None]]]
    """
    reader = (int(d) if d is not '.' else None for d in dotstring)

    def read():
        n = next(reader)
        if n:
            return [n, read(), read()]
        else:
            return None
    return read()


def tree_dotstring(tree):
    """
    Problem 69b

    >>> tree_dotstring([1, [2, [4, None, None], [5, None, None]], [3, None, \
[6, [7, None, None], None]]])
    '124..5..3.67...'
    """
    result = []

    def traverse(tree):
        if tree is None:
            result.append('.')
        else:
            result.append(str(tree[0]))
            traverse(tree[1])
            traverse(tree[2])

    traverse(tree)
    return "".join(result)


def ismultiwaytree(tree):
    """
    Problem 70B

    >>> ismultiwaytree((t(a,[t(f,[t(g,[])]),t(c,[]),t(b,[t(d,[]),t(e,[])])])))
    True
    """
    return isinstance(tree[0], int) and all(ismultiwaytree(s) for s in tree[1])


def nnodes(tree):
    """
    Problem 70C

    >>> nnodes(t(a,[t(f,[])]))
    2
    """
    return 1 + sum(nnodes(n) for n in tree[1])


def string_multiwaytree(string):
    """
    Problem 70D

    >>> string_multiwaytree('167^^3^24^5^^^')
    [1, [[6, [[7, []]]], [3, []], [2, [[4, []], [5, []]]]]]
    """
    reader = (int(d) if d is not '^' else None for d in string)

    def read():
        value = next(reader)
        if not value:
            return
        nodes = []
        node = read()
        while node:
            nodes.append(node)
            node = read()
        return [value, nodes]

    return read()


def multiwaytree_string(tree):
    """
    Problem 70E

    >>> multiwaytree_string([1, [[6, [[7, []]]], [3, []], [2, [[4, []], [5,\
[]]]]]])
    '167^^3^24^5^^^'
    """
    result = []

    def traverse(tree):
        result.append(str(tree[0]))
        for node in tree[1]:
            traverse(node)
        result.append('^')

    traverse(tree)
    return "".join(result)


def ipl(tree):
    """
    Problem 71

    >>> ipl([1, [[6, [[7, []]]], [3, []], [2, [[4, []], [5,\
[]]]]]])
    9
    """
    paths = []

    def traverse(tree, depth=1):
        if len(tree[1]) == 0:
            return 0
        else:
            for node in tree[1]:
                paths.append(depth)
                traverse(node, depth + 1)

    traverse(tree)

    return sum(paths)


def tree_ltl(tree):
    """
    Problem 73a

    >>> tree_ltl(t(a,[t(b,[t(c,[])])]))
    ['(', 0, '(', 1, 2, ')', ')']
    >>> tree_ltl([1, [[6, [[7, []]]], [3, []], [2, [[4, []], [5,\
[]]]]]])
    ['(', 1, '(', 6, 7, ')', 3, '(', 2, 4, 5, ')', ')']
    """
    result = []

    def traverse(tree):
        value = tree[0]
        nodes = tree[1]
        if len(nodes) == 0:
            result.append(value)
        else:
            result.append('(')
            result.append(value)
            if len(nodes) == nnodes(tree) - 1:
                for node in nodes:
                    result.append(node[0])
            else:
                for node in nodes:
                    traverse(node)
            result.append(')')
    traverse(tree)
    return result


def ltl_tree(ltl):
    """
    Problem 73B

    >>> ltl_tree(['(', 0, '(', 1, 2, ')', ')'])
    [0, [[1, [[2, []]]]]]
    >>> ltl_tree(['(', 1, '(', 6, 7, ')', 3, '(', 2, 4, 5, ')', ')'])
    [1, [[6, [[7, []]]], [3, []], [2, [[4, []], [5, []]]]]]
    """
    reader = iter(ltl)

    def read():
        n = next(reader)
        if n == '(':
            value = next(reader)
            result = []
            next_result = read()
            while next_result is not None:
                result.append(next_result)
                next_result = read()
            return [value, result]
        elif n == ')':
            return None
        else:
            return [n, []]

    return read()
