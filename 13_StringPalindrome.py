word = input("Enter a word: ")

start = 0
end = len(word) - 1

is_palindrome = True

while start < end:
    if word[start] != word[end]:
        is_palindrome = False
        break

    start += 1
    end -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")