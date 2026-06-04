print("=" * 50)
print("\t  ^_____^ TO DO LIST ^_____^")
print("=" * 50)

tasks = []

while True:

    print("\n" + "-" * 50)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("-" * 50)

    choice = input("What do you want to do?: ")

    while True:
        if choice not in ["1", "2", "3", "4"]:
            print("Please pick a valid Choice Option (1, 2, 3 or 4).")
            choice = input("What do you want to do?: ")
        else:
            break

    if choice == "1":
        task = input("\nGo ahead, add a task: ")
        tasks.append(task)
        print("Task added!")

        input("\nPress Enter to continue...")

    elif choice == "2":
        if len(tasks) == 0:
            print("\nNo tasks found!")
        else:
            print(f"\nYou currently have {len(tasks)} task(s) pending:\n")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

        input("\nPress Enter to continue...")

    elif choice == "3":
        if len(tasks) == 0:
            print("\nNo tasks found!")

        else:
            print(f"\nYou currently have {len(tasks)} task(s) pending:\n")

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            dlt = int(input("\nWhich task do you want to delete?: "))

            if 1 <= dlt <= len(tasks):
                tasks.pop(dlt - 1)
                print(f"Task number {dlt} deleted successfully!")
            else:
                print("Invalid task number!")

        input("\nPress Enter to continue...")

    elif choice == "4":
        print("\nSee you later, Keep Working!")
        break