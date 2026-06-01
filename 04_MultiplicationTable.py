#Wap to print multiplication table of a number

n = int(input("Enter the number: "))

print(f"Multiplication Table of {n} is:")

for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")