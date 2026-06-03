import random
import time

choices = ["rock", "paper", "scissors"]

while True:

    print("\n" + "=" * 40)
    print("        ROCK PAPER SCISSORS")
    print("          First to 3 Wins")
    print("=" * 40)

    time.sleep(1)

    userSCORE = 0
    systemSCORE = 0

    while userSCORE < 3 and systemSCORE < 3:

        while True:
            pick = input("\nChoose (rock/paper/scissors): ").lower()

            if pick not in choices:
                print("Please enter rock, paper, or scissors.")
            else:
                break

        system = random.choice(choices)

        print("\n" + "-" * 40)
        print(f"You      : {pick}")
        print(f"Computer : {system}")
        print("-" * 40)

        if system == pick:
            print("It's a tie!")

        elif (
            (pick == "rock" and system == "scissors")
            or
            (pick == "paper" and system == "rock")
            or
            (pick == "scissors" and system == "paper")
        ):
            print("You win this round!")
            userSCORE += 1

        else:
            print("Computer wins this round!")
            systemSCORE += 1

        print(f"\nScore: You {userSCORE} - {systemSCORE} Computer")

        time.sleep(1)

    print("\n" + "=" * 40)
    print("            FINAL RESULT")
    print("=" * 40)
    print(f"Your Score     : {userSCORE}")
    print(f"Computer Score : {systemSCORE}")
    print("=" * 40)

    if userSCORE > systemSCORE:
        print("Congratulations! You Won!")
    else:
        print("You Lost! Better luck next time!")

    while True:
        again = input("\nPlay Again? (y/n): ").lower()

        if again not in ["y", "n"]:
            print("Please enter y or n.")
        else:
            break

    if again == "n":
        print("\nThanks for playing!")
        break
