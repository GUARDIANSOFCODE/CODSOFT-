import json


# File to store tasks

TODO_FILE = "todo_list.json"

# Load tasks from file

def load_tasks():
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    task = input("Enter the new task: ")
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

# View all tasks

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            status = "✔" if task["completed"] else "✘"
            print(f"{idx}. {task['task']} [{status}]")

# Update a task

def update_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_num = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_num < len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[task_num]["task"] = new_task
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Mark a task as completed

def complete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task

def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            del tasks[task_num]
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu

def todo_list():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

# Run the to-do list app
todo_list()
