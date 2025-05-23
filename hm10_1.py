from inspect import isgenerator


def pows(x):
    return x**2


def some_gen(begin, end, func):
    current = begin
    for _ in range(end):
        yield current
        current = func(current)


gen = some_gen(2, 4, pows)
assert isgenerator(gen) == True
assert list(gen) == [2, 4, 16, 256]
print("OK")
