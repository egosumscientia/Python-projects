import json

from scripts.regsetup import description

TASKS_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from a JSON file."""
    try:
        with open(TASKS_FILE, "r") as f:
            return json.loads(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Saves tasks to a JSON file"""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

def add_task(tasks, name, description):
    """Adds a new task to the list"""
    tasks.append({"name": name, "description": description, "completed": False})
    save_tasks(tasks)

def complete_task(tasks, name):
    """Marks a task as completed"""
    for task in tasks:
        if task["name"].lower() == name.lower():
            task["completed"] = True
            save_tasks(tasks)
            print(f"Task '{name}' marked as completed.")
            return
    print(f"No task found with the name: {name}")

def show_tasks(tasks):
    """Displays all tasks"""
    if not tasks:
        print("No tasks available.")
        return

    print("\n **Task List**")
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f"{task['name']}: {task['description']} [{status}]")


def menu():
    """Displays te task manager menu"""
    tasks = load_tasks()

    while True:
        print("\n=== Task Manager Menu ===")
        print("1. Add task")
        print("2. Mark task as completed")
        print("3. Show tasks")
        print("4. Exit")

        option = input("Choose an option")

        if option == "1":
            name = input("Task name: ")
            description = input("Task description: ")
            add_task(tasks, name, description)

        elif option == "2":
            name = input("Task name to mark as completed: ")
            complete_task(tasks, name)

        elif option == "3":
            show_tasks(tasks)

        elif option == "4":
            print("Goodbye!")
            break

        else:
            print("Wrong option, please try again")

#Run the program
if __name__ == "__main__":
    menu()