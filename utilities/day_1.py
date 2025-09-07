"""
Challenge: Self-Intro Script Generator

Create a Python script that interacts with the user and generates a personalized self-introduction.

Your program should:
1. Ask the user for their name, age, city, profession, and favorite hobby.
2. Format this data into a warm, friendly paragraph of self-introduction.
3. Print the final paragraph in a clean and readable format.

Example:
If the user inputs:
  Name: Priya
  Age: 22
  City: Jaipur
  Profession: Software Developer
  Hobby: playing guitar

Your script might output:
  "Hello! My name is Priya. I'm 22 years old and live in Jaipur. I work as a Software Developer and I absolutely enjoy playing guitar in my free time. Nice to meet you!"

Bonus:
- Add the current date to the end of the paragraph like: "Logged on: 2025-06-14"
- Wrap the printed message with a decorative border of stars (*)
"""

#### Solution

import datetime

name: str = input("What is your name ? ").strip().capitalize()
age: int = int(input("How old are you ? "))
city: str = input("Which city do you live in ? ").strip().capitalize()
profession: str = input("What is your profession ? ")
hobby: str = input("What is your hobby ? ")

template_introduction: str = f"Hello, my name is {name}. I'm {age} years old and live in {city}. I work as a/an {profession} and I absolutely enjoy {hobby} in my leisure time."

current_date: str = datetime.date.today().isoformat()
intro_msg: str = f"Logged in on : {current_date}\n"


intro_msg += template_introduction

header: str = "*" * 50
footer: str = "*" * 50
print(f"\n{header}\n{intro_msg}\n{footer}")
