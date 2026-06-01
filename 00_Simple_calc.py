# Wap to make a Simple calculator

print("!!-----------Welcome to the Calculator-----------!!")

opt = input("Choose an operator(+,-,*,/): ")

num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))


if opt == "+" :
    print(f"Result = {num1 + num2}")
elif opt == "-" :
    print(f"Result = {num1 - num2}")
elif opt == "*" :
    print(f"Result = {num1 * num2}")
elif opt == "/" :
    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        print(f"Result = {num1 / num2}")
else:
    print("Invalid operator.")


















