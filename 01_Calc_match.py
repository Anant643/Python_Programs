#Simple calculator using Match Statement

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

opt = input("Choose an operator (+,-,*,/): ")

match opt:

    case "+":
        print(f"Result = {num1 + num2}")

    case "-":
        print(f"Result = {num1 - num2}")

    case "*":
        print(f"Result = {num1 * num2}")

    case "/":
        print(f"Result = {num1 / num2}")

    case _:
        print("Invalid operator")