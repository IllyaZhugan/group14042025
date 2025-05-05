def calculator():

    while True:
        num1 = float(input("Введіть перше число: "))
        operation = input("Введіть операцію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Ділення на нуль неможливе!")
                continue
            result = num1 / num2
        else:
            print("Невідома операція!")
            continue

        print(f"Результат: {result}")

        again = input("Хочете продовжити? (y/yes для продовження): ").lower()
        if again not in ["y", "yes"]:
            print("Дякуємо за користування калькулятором!")
            break


calculator()
