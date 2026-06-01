print("!!--------Weight Converter--------!!")

while True:
    unit = input("What is the unit of your Weight (KG or LB)?: ").upper()

    if unit != "KG" and unit != "LB":
        print("Please enter a valid unit.")
    else:
        break

if unit == "KG":
    weight = float(input(f"Enter your Weight in {unit}: "))

    pounds = weight * 2.20462

    print(f"{weight} KG = {pounds:.2f} LB")

else:
    weight = float(input(f"Enter your Weight in {unit}: "))

    kilograms = weight / 2.20462

    print(f"{weight} LB = {kilograms:.2f} KG")