from abc import ABC, abstractmethod
import csv
import json

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class StorageHandler(ABC):
    @abstractmethod
    def save(self, tasks, filename):
        pass

    @abstractmethod
    def load(self, filename):
        pass

class CSVStorageHandler(StorageHandler):
    def save(self, tasks, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])

    def load(self, filename):
        tasks = []
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(Task(row["Task ID"], row["Title"], row["Description"], row["Due Date"], row["Status"]))
        return tasks

class JSONStorageHandler(StorageHandler):
    def save(self, tasks, filename):
        task_list = []
        for task in tasks:
            task_list.append({
                "task_id": task.task_id,
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date,
                "status": task.status
            })
        with open(filename, 'w') as file:
            json.dump(task_list, file, indent=4)

    def load(self, filename):
        tasks = []
        with open(filename, 'r') as file:
            task_list = json.load(file)
            for task_data in task_list:
                tasks.append(Task(task_data["task_id"], task_data["title"], task_data["description"], task_data["due_date"], task_data["status"]))
        return tasks

class TaskManager:
    def __init__(self, storage_handler):
        self.tasks = []
        self.storage_handler = storage_handler

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def update_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task.task_id == task_id:
                for key, value in kwargs.items():
                    setattr(task, key, value)
                return True
        return False

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def filter_tasks(self, status):
        return [task for task in self.tasks if task.status == status]

    def save_tasks(self, filename):
        self.storage_handler.save(self.tasks, filename)

    def load_tasks(self, filename):
        self.tasks = self.storage_handler.load(filename)

def main():
    storage_handler = CSVStorageHandler()  # Change to JSONStorageHandler() for JSON format
    task_manager = TaskManager(storage_handler)

    while True:
        print("\nWelcome to the To-Do Application!")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Filter tasks by status")
        print("6. Save tasks")
        print("7. Load tasks")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            status = input("Enter Status (Pending/In Progress/Completed): ")
            task = Task(task_id, title, description, due_date, status)
            task_manager.add_task(task)
            print("Task added successfully!")

        elif choice == '2':
            print("Tasks:")
            task_manager.view_tasks()

        elif choice == '3':
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new Title (leave blank to skip): ")
            description = input("Enter new Description (leave blank to skip): ")
            due_date = input("Enter new Due Date (YYYY-MM-DD) (leave blank to skip): ")
            status = input("Enter new Status (Pending/In Progress/Completed) (leave blank to skip): ")
            updates = {}
            if title: updates['title'] = title
            if description: updates['description'] = description
            if due_date: updates['due_date'] = due_date
            if status: updates['status'] = status
            if task_manager.update_task(task_id, **updates):
                print("Task updated successfully!")
            else:
                print("Task not found!")

        elif choice == '4':
            task_id = input("Enter Task ID to delete: ")
            task_manager.delete_task(task_id)
            print("Task deleted successfully!")

        elif choice == '5':
            status = input("Enter status to filter by (Pending/In Progress/Completed): ")
            filtered_tasks = task_manager.filter_tasks(status)
            for task in filtered_tasks:
                print(task)

        elif choice == '6':
            filename = input("Enter filename to save tasks: ")
            task_manager.save_tasks(filename)
            print("Tasks saved successfully!")

        elif choice == '7':
            filename = input("Enter filename to load tasks: ")
            task_manager.load_tasks(filename)
            print("Tasks loaded successfully!")

        elif choice == '8':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()