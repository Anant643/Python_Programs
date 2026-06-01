#Wap to find the greatest among 3 numbers

num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))

num3 = float(input("Enter third number: "))


if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the greatest among all.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the greatest among all.")
else:
    print(f"{num3} is the greatest among all.")
