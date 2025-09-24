"""
 Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""

import os

# Load the tasks
TASK_FILE: str = "tasks.txt"


def load_tasks_from_file():
    tasks = []
    if not os.path.exists(TASK_FILE):
        print("No tasks file found.")
    else:
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            for line in f:
                text, status = line.strip().rsplit("||", 1)
                tasks.append({"text": text, "done": status == "done"})
    return tasks


def save_tasks_to_file(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            f.write(f"{task['text']} || {status}\n")


def display_tasks(tasks):
    if not tasks:
        print("No tasks found")
    else:
        for i, task in enumerate(tasks, 1):
            checkbox = "✅" if task["done"] else " "
            print(f"{i}. [{checkbox}] {task['text']}")
    print()


def task_manager():
    tasks = load_tasks_from_file()

    while True:
        print("\n -------- Terminal Task Manager-------")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5) ").strip()

        match choice:
            case "1":  # Add tasks
                text = input("Enter your task ").strip()
                if text:
                    tasks.append({"text": text, "done": False})
                    save_tasks_to_file(tasks)
                else:
                    print("Task cannot be empty ")

            case "2":  # View Tasks
                display_tasks(tasks)
            case "3":  # Mark Task as compeleted
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number "))
                    if 1 <= num <= len(tasks):
                        tasks[num - 1]["done"] = True
                        save_tasks_to_file(tasks)
                        print("Task marked as done")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a number")

            case "4":  # Delele task
                display_tasks(tasks)
                try:
                    num = int(input("Enter the task number to delete "))
                    if 1 <= num <= len(tasks):
                        removed_task = tasks.pop(num - 1)
                        save_tasks_to_file(tasks)
                        print(f"{removed_task['text']} Task removed ")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a number")

            case "5":
                print("Exiting the task manager\n-----Good Bye-----")
                break

            case _:
                print("Please choose a valid option")


if __name__ == "__main__":
    task_manager()
