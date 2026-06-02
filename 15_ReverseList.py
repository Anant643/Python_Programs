# reversing list

size = int(input("Enter size of list: "))

mylist =[]

for i in range(size):
    num = int(input("Enter a number:"))
    mylist.append(num)

reversed_nums = []

for item in mylist:
    reversed_nums = [item] + reversed_nums

print("Reversed list is:-")
print(reversed_nums)