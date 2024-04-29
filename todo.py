import json
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, title, priority, due_date=None):
    task = {"title": title, "priority": priority, "completed": False, "due_date": due_date}
    tasks.append(task)

def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        del tasks[index]

def mark_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Not Done"
        due_date = task["due_date"] if task["due_date"] else "No due date"
        print(f"{i+1}. {task['title']} \n Priority: {task['priority']}\n Status: {status}\n Due Date: {due_date}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            list_tasks(tasks)
            title = input("Enter task title: ")
            priority = input("Enter task priority (high/medium/low): ")
            due_date_str = input("Enter due date (YYYY-MM-DD) or leave blank if none: ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            add_task(tasks, title, priority, due_date)
            save_tasks(tasks)
            print("Task added successfully.")
        elif choice == "2":
            list_tasks(tasks)
            index = int(input("Enter task number to remove: ")) - 1
            remove_task(tasks, index)
            save_tasks(tasks)
            print("Task removed successfully.")
        elif choice == "3":
            list_tasks(tasks)
            index = int(input("Enter task number to mark as completed: ")) - 1
            mark_completed(tasks, index)
            save_tasks(tasks)
            print("Task marked as completed.")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
