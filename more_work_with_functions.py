def is_numbers_more_than_6(number) -> bool:
    return number > 6


def generate_infinity_sequence(func):
    # print("give 1")
    # yield 1
    # print("rest")
    # yield 2
    # print("last")
    current = 1
    while True:
        yield current
        print(func(current))
        current += 1


infinity = generate_infinity_sequence(is_numbers_more_than_6)

print(next(infinity))
print(565656566)
print(next(infinity))
print(next(infinity))
