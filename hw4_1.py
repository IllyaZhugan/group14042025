def zeros_to_end(lst):
    insert_pos = 0

    for num in lst:
        if num != 0:
            lst[insert_pos] = num
            insert_pos += 1

    for i in range(insert_pos, len(lst)):
        lst[i] = 0


examples = [
    [0, 1, 0, 12, 3],
    [0],
    [1, 0, 13, 0, 0, 0, 5],
    [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0],
]

for ex in examples:
    zeros_to_end(ex)
    print(ex)
