#Wap to count vowels in a sentence

sentence = input("Enter a sentence: ")

count = 0
vowels = "aeiouAEIOU"

for ch in sentence:
    if ch in vowels:
        count += 1

print(f"Total vowels = {count}")