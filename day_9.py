"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time
import winsound

while True:
    try:
        input_time_in_seconds: int = int(input("⏰ Enter the time in seconds : "))

        if input_time_in_seconds < 1:
            print("Please enter a time greater than 0")
            continue  # Keep asking till the user provides a number greater than 0
        break  # Proceed with the given timer

    except ValueError:
        print("Invalid input. Enter a whole number")

print("\n⏲️ Timer Started...")

for remaining_time in range(input_time_in_seconds, 0, -1):
    mins, secs = divmod(remaining_time, 60)
    print(f"⌛Time left : {mins:02}:{secs:02}", end="\r")
    time.sleep(1)

# Timer expired
frequency = 3000  # 3000 Hertz
duration = 1000  # 1000ms = 1 second

print("\nTime's up!")
winsound.Beep(frequency, duration)
