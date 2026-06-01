import time

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total_seconds = hours * 3600 + minutes * 60 + seconds

for current in range(total_seconds, -1, -1):
    hrs = current // 3600
    mins = (current % 3600) // 60
    secs = current % 60

    print(f"{hrs:02d}:{mins:02d}:{secs:02d}")

    time.sleep(1)

print("⏰ Time's up!")