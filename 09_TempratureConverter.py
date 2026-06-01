print("!!--------Temperature Converter--------!!")

while True:
    unit = input("What is the unit of your Temperature (F or C)?: ").upper()

    if unit != "F" and unit != "C":
        print("Please enter a valid unit.")
    else:
        break


if unit == "F":
    temp = float(input(f"Enter your Temperature in {unit}: "))

    celsius = (temp - 32) * 5 / 9

    print(f"{temp}°F = {celsius:.2f}°C")

else:
    temp = float(input(f"Enter your Temperature in {unit}: "))

    fahrenheit = (temp * 9 / 5) + 32

    print(f"{temp}°C = {fahrenheit:.2f}°F")

print("Have a great day^_^")