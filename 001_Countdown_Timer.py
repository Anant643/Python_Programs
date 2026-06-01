import time

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total_seconds = hours * 3600 + minutes * 60 + seconds

for remaining_seconds in range(total_seconds, -1, -1):

    hrs = remaining_seconds // 3600
    mins = (remaining_seconds % 3600) // 60
    secs = remaining_seconds % 60

    print(f"{hrs:02d}:{mins:02d}:{secs:02d}")

    time.sleep(1)

print("⏰ Time's up!")
