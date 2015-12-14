def try_input(prompt, conversion=int):
    while True:
        try:
            inp = input(prompt)
            return conversion(inp)
        except:
            pass


if __name__ == "__main__":
    p = 23
    g = 5

    print("p: {}, g: {}".format(p, g))
    a = try_input("Alice's secret number: ")
    print("Alice chose {} as her secret number.".format(a))
    A = g ** a % p
    print("A = {g}^{a} mod {p} = {A}".format(**locals()))
    print("Alice sent Bob A!")

    b = try_input("Bob's secret number: ")
    print("Bob chose {} as his secret number.".format(b))
    B = g ** b % p
    print("B = {g}^{b} mod {p} = {B}".format(**locals()))
    print("Bob sent Alice B!")

    print("Alice is calculating her shared secret...")
    s_a = B ** a % p
    print("s = {B} ^ {a} mod {p} = {s_a}".format(**locals()))

    print("Bob is calculating his shared secret...")
    s_b = A ** b % p
    print("s = {A} ^ {b} mod {p} = {s_b}".format(**locals()))

    assert s_a == s_b

    print("Both secrets match!")
