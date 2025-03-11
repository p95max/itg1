import json
import os

class Task:
    def __init__(self, name, info, status = "task is not done"):
        self.name = name
        self.info = info
        self.status = status

    def __str__(self):
        return f"{self.name}-{self.info} ({self.status})"

    def done(self):
        self.status = "task is done"

    def undone(self):
        self.status = "task is not done"

class TaskManager:
    tasks_storage = "tasks.json"

    def __init__(self):
        self.tasks_list = []
        self.load_tasks()

    def add_task(self, name, info, status="task is not done"):
        name = name.lower()
        info = info.lower()
        status = status.lower()
        task = Task(name, info, status)
        self.tasks_list.append(task)
        print(f"Task {name} added to task list")
        self.save_tasks()

    def remove_task(self, task_name):
        self.tasks_list = [task for task in self.tasks_list if task.name != task_name]
        print(f"Task '{task_name}' was deleted")
        self.save_tasks()

    def change_task_status(self, task_name, is_done: bool):
        for task in self.tasks_list:
            if task.name == task_name:
                task.done() if is_done else task.undone()
                self.save_tasks()
                return True
        return False

    def show_tasks(self):
        if not self.tasks_list:
            print("No tasks in the list")
        else:
            print("\n".join(str(task) for task in self.tasks_list))

    def save_tasks(self):
        tasks_data = [(task.name, task.info, task.status) for task in self.tasks_list]
        with open(self.tasks_storage, "w") as file:
            json.dump(tasks_data, file, indent=4)

    def read_tasks_from_file(self):
        if os.path.exists(self.tasks_storage) and os.path.getsize(self.tasks_storage) > 0:
            with open(self.tasks_storage, "r") as file:
                return json.load(file)
        return []

    def load_tasks(self):
        try:
            with open(self.tasks_storage, "r") as file:
                tasks_data = json.load(file)
            self.tasks_list = [Task(name, info, status) for name, info, status in tasks_data]
            print("Tasks were loaded")
        except FileNotFoundError:
            print(f"File {self.tasks_storage} not found")

    def clear_tasks(self):
        self.tasks_list = []
        self.save_tasks()
        print("All tasks were deleted!")

mananger = TaskManager()

while True:
    user_input = input(
        "1. Show current tasks.\n"
        "2. Add new task.\n"
        "3. Delete task.\n"
        "4. Change task status.\n"
        "5. Clear tasks list.\n"
        "6. Exit.\n"
    )

    match user_input:

        case "1":
            mananger.show_tasks()
        case "2":
            name = input("Enter task name: ")
            info = input("Enter task info: ")
            mananger.add_task(name, info)
        case "3":
            task_name = input("Enter task name for deleting: ")
            mananger.remove_task(task_name)
        case "4":
            task_name = input("Enter task name for status changing: ")
            new_status = input("Enter new status(done/not done): ")
            mananger.change_task_status(task_name, new_status == "done")
        case "5":
            mananger.clear_tasks()
        case "6":
            print("Exiting program")
            break

        case _:
            print("Invalid option, please try again.")
