import json
import csv

def total_tasks(tasks):         # counts total tasks
    return len(tasks)

def completed_tasks(tasks):     # counts completed tasks
    return sum(1 for task in tasks if task['completed'])

def pending_tasks(tasks):       # counts pending tasks
    return sum(1 for task in tasks if not task['completed'])

def avg_priority(tasks):        # calculates average priority
    if not tasks:
        return 0
    return sum(task['priority'] for task in tasks) / len(tasks)

def convert_to_csv(tasks, filename="tasks.csv"):    # converts JSON data to CSV
    with open(filename, "w", newline="") as file:
        fieldnames = ["ID", "Task", "Completed", "Priority"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow({
                "ID": task["id"],
                "Task": task["task"],
                "Completed": task["completed"],
                "Priority": task["priority"]
            })

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    print("Error: tasks.json file not found.")
    tasks = []


print("Total tasks:", total_tasks(tasks))
print("Completed tasks:", completed_tasks(tasks))
print("Pending tasks:", pending_tasks(tasks))
print("Average Priority level:", f"{avg_priority(tasks):.2f}")

convert_to_csv(tasks)
print("\nTasks successfully saved to tasks.csv!")