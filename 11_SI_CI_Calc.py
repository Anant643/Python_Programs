print("!!--------SI & CI Calculator--------!!")

while True:
    p = float(input("Enter Principal Amount: "))

    if p <= 0:
        print("Principal must be positive.")
    else:
        break

while True:
    r = float(input("Enter Rate of Interest (%): "))

    if r <= 0:
        print("Rate must be positive.")
    else:
        break

while True:
    t = float(input("Enter Time (years): "))

    if t <= 0:
        print("Time must be positive.")
    else:
        break

si = (p * r * t) / 100

amount = p * (1 + r / 100) ** t
ci = amount - p

print("\n----- Results -----")
print(f"Simple Interest   = {si:.2f}")
print(f"Amount            = {amount:.2f}")
print(f"Compound Interest = {ci:.2f}") 