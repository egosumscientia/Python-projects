"""Allows users to add tasks with a name and description.
Allows users to mark tasks as completed.
Displays all tasks (pending and completed).
Saves tasks to a JSON file for persistence.
Loads tasks automatically when the program starts."""

import json

from scripts.regsetup import description
from sqlalchemy import false
from sqlalchemy.util import ellipses_string


class Task:
    """Represents a task with a name, description, and completion status"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed =  False #By default, a new task is not completed.

    def mark_completed(self):
        """Marks the task as completed"""
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.name}: {self.description} [{status}]"

class TaskManager:
    """Manages the task list and provides operations to manipulate tasks"""

    def __init__(self):
        self.tasks = []
        self.file = "tasks.json"
        self.load_tasks()

    def add_task(self, name, description):
        """Adds a new task to the list."""
        new_task = Task(name, description)
        self.tasks.append(new_task)
        self.save_tasks()

    def complete_task(self, name):
        """Marks a task as completed if it exists in the list"""
        for task in self.tasks:
            if task.name.lower() == name.lower():
                task.mark_completed()
                self.save_tasks()
                print(f"Task '{name}' marked as completed.")
                return
        print(f"No task found with the name: {name}")

    def show_tasks(self):
        """Displays all tasks in the list."""
        if not self.tasks:
            print("No tasks available.")
            return

        print("\n **Task List**")
        for task in self.tasks:
            print(task)

    def save_tasks(self):
        """Saves the tasks to a JSON file for persistence"""
        with open(self.file, "w") as f:
            json.dump([task.__dict__ for task in self.tasks], f)

    def load_tasks(self):
        """Loads tasks from the JSON file when the program starts"""
        try:
            with open(self.file, "r") as f:
                loaded_tasks = json.load(f)
                self.tasks = [Task(t["name"], t["description"]) for t in loaded_tasks]
                for task, data in zip(self.tasks, loaded_tasks):
                    task.completed = data["completed"]
        except FileNotFoundError:
            self.tasks = []

def menu():
    """Displays an interactive menu to manage tasks"""
    manager = TaskManager()

    while True:
        print("\n=== Task Manager Menu ===")
        print("1. Add task")
        print("2. Mark task as completed")
        print("3. Show tasks")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == "1":
            name =  input("Task name: ")
            description = input("Task description: ")
            manager.add_task(name, description)

        elif option == "2":
            name = input("Task name to mark as completed: ")
            manager.complete_task(name)

        elif option == "3":
            manager.show_tasks()

        elif option == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")


#Run the program
if __name__ == "__main__":
    menu()















