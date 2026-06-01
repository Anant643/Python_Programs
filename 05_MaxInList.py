#Wap to find the larget number in a list

size = int(input("How many numbers?: "))

mylist = []

for i in range(size):
    num = int(input("Enter a number: "))
    mylist.append(num)

minm = mylist[0]
maxm = mylist[0]

for i in mylist:
    if i > maxm:
        maxm = i
    if i < minm:
        minm = i

print(f"biggest number is {maxm}")
print(f"smallest number is {minm}")