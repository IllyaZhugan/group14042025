num = 1234

num1 = num // 1000
num2 = (num - num1 * 1000) // 100
num3 = (num % 100) // 10
num4 = (num % 10)

print(num1)
print(num2)
print(num3)
print(num4)

pass