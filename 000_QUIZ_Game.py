score = 0

quiz = {
    "Capital of Japan?": "tokyo",
    "Largest planet in the Solar System?": "jupiter",
    "2 + 2?": "4",
    "Color of grass?": "green",
    "Creator of Python?": "guido van rossum"
}

while True:

    score = 0

    print("\n=== QUIZ GAME ===\n")

    for question, answer in quiz.items():

        user = input(question + " ").strip().lower()

        if user == answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {answer}\n")

    percentage = (score / len(quiz)) * 100

    print("=" * 30)
    print(f"Score: {score}/{len(quiz)}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage == 100:
        print("Perfect Score! 🌟")
    elif percentage >= 80:
        print("Great Job! 🎉")
    elif percentage >= 60:
        print("Good Work! 👍")
    else:
        print("Keep Practicing! 💪")

    print("=" * 30)

    again = input("\nPlay again? (yes/no): ").strip().lower()

    if again != "yes":
        print("Thanks for playing!")
        break