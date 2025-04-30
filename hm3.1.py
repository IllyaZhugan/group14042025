num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

operation = input("Введіть дію (+, -, *, /): ")


if operation == "+":
    result = num1 + num2
    print("Результат:", result)
elif operation == "-":
    result = num1 - num2
    print("Результат:", result)
elif operation == "*":
    result = num1 * num2
    print("Результат:", result)
elif operation == "/":
    if num2 == 0:
        print("Помилка: ділення на нуль неможливе")
    else:
        result = num1 / num2
        print("Результат:", result)
else:
    print("Помилка: невідома операція")

    pass
