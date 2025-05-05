def even_index_sum_last(numbers):
    if not numbers:
        return 0

    even_index_sum = sum(num for idx, num in enumerate(numbers) if idx % 2 == 0)
    return even_index_sum * numbers[-1]


examples = [[0, 1, 7, 2, 4, 8], [1, 3, 5], [6], []]

for ex in examples:
    result = even_index_sum_last(ex)
    print(f"{ex} => {result}")
