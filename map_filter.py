some_list = [5, 6, 77, 7, 8, 9]


def is_numbers_more_than_5(number) -> bool:
    return number > 5


def is_numbers_more_than_6(number) -> bool:
    return number > 6


callable_validator = {
    5: is_numbers_more_than_5,
    6: is_numbers_more_than_6,
    "Lambda": lambda arg: lambda: lambda number: number * 5,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
}

n1 = 10
n2 = 20
operation = "-"
res_lambda = callable_validator[operation](n1, n2)


res = callable_validator["Lambda"](5)()(5)

# wantad_func = 6
# for item in some_list:
#     func = callable_validator[wantad_func](item)

# filtered_data = filter(is_numbers_more_than_5, some_list)
filtered_data = filter(lambda number: number > 5, some_list)
mapped_data = list(map(lambda number: number * 2, filtered_data))
# some_list.insert(0, 50000)

# print(next(mapped_data))
#
# print(next(filtered_data))
# print(list(filtered_data))
pass
