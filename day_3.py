"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400
  Neha owes ₹400
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""

num_people: int = int(input("How many people are there in the group ? "))
member_names: list[str] = []

for idx in range(num_people):
    name: str = input(f"What is the name of the member #{idx + 1} ? ").strip()
    member_names.append(name)

total_bill: float = float(input("Please enter the total bill amount : "))
share: float = round(total_bill / num_people, 3)
print("\n")
print(f"{'*' * 10} Bill Calculator{'*' * 10}")
print(f"Total bill : {total_bill}")
for member in member_names:
    print(f"Share of {member} : ${share}")
