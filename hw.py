number = int(input("Введіть 4-значне число: "))
num1 = (number // 1000)
num2 = (number % 1000) // 100
num3 = (number % 100) // 10
num4 = (number % 10)

print(num1)
print(num2)
print(num3)
print(num4)
