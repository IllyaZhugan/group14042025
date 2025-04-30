def first_list(lst):
    if len(lst) <= 1:
        return lst
    else:
        return [lst[-1]] + lst[:-1]


print(first_list([12, 3, 4, 10]))
print(first_list([1]))
print(first_list([]))
print(first_list([12, 3, 4, 10, 8]))

pass
