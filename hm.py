import random

secret_number = random.randint(1, 100)
guess = None
attempts = 0

print("I am thinking of a number between 1 and 100.")

while guess != secret_number:
    try:
        guess = int(input("Take a guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
    except ValueError:
        print("Please enter a valid number.")   