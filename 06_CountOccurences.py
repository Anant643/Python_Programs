# Count how many times a specific number appears in a list


size = int(input("Enter size of list: "))

mylist =[]

for i in range(size):
    num = int(input("Enter a number:"))
    mylist.append(num)

count = 0
target = int(input("Which number do you want to check: "))

for i in (mylist):
    if i == target:
        count+=1


print(f"Total occurence of {target} in the list is {count}")