import random

numbers = [random.randint(1, 100) for i in range(random.randint(3, 10))]

result = [numbers[0], numbers[2], numbers[-2]]

print("Початковий список:", numbers)
print("Новий список:", result)

pass

