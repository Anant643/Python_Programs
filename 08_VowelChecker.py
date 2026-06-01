#Wap to check whether entered character is vowel
ch = input("Enter a character: ")
count = 0
vowels = "aeiouAEIOU"

for i in vowels:
    if i == ch:
        count += 1

if count == 1:
    print(f"Entered character {ch} is a vowel.")
else:
    print(f"Entered character {ch} is not a vowel.")