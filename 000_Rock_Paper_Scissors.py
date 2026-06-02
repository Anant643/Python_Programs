import random
import time

choices = ["rock", "paper", "scissors"]

while True:

    print("First to 3 Wins takes the DUB!")
    time.sleep(1)
    print("Here we go then!")
    print()
    time.sleep(1)

    userSCORE = 0
    systemSCORE = 0

    while userSCORE < 3 and systemSCORE < 3:

        while True:
            pick = input("Rock, Paper or Scissors? Shoot!: ").lower()

            if pick not in ["rock", "paper", "scissors"]:
                print("Pick a valid choice to play!")
            else:
                break

        system = random.choice(choices)

        print(f"You Chose {pick}!")
        print(f"The computer chose {system}!")

        if system == pick:
            print("Ooh, Tied!")

        elif (
            (pick == "rock" and system == "scissors")
            or
            (pick == "paper" and system == "rock")
            or
            (pick == "scissors" and system == "paper")
        ):
            print("You win!")
            userSCORE += 1

        else:
            print("Computer wins!")
            systemSCORE += 1

        print(f"Score -> You: {userSCORE} | Computer: {systemSCORE}")
        print()
        print()

    print("---------HERE ARE THE RESULTS----------")
    time.sleep(1)
    print(f"Your Score: {userSCORE}")
    print(f"System's Score: {systemSCORE}")

    if userSCORE > systemSCORE:
        print("Good Game! You Won!")
    else:
        print("Haha You lost! Better luck next time!")

    while True:
        again = input("\nPlay Again? (y/n): ").lower()

        if again not in ["y", "n"]:
            print("Please enter y or n.")
        else:
            break

    if again == "n":
        print("Thanks for playing!")
        break




