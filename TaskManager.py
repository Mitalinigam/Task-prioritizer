from datetime import datetime

class Task:
    def __init__(self, title, deadline, priority):
        self.title = title
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.priority = int(priority)
        self.completed = False

    def __str__(self):
        status = "✅ Done" if self.completed else "⏳ Pending"
        return f"{self.title} | Due: {self.deadline.date()} | Priority: {self.priority} | {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, deadline, priority):
        self.tasks.append(Task(title, deadline, priority))
        print("Task added!\n")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.\n")
            return
        print("\n--- All Tasks ---")
        sorted_tasks = sorted(
            self.tasks,
            key=lambda x: (x.completed, x.deadline, x.priority)
        )
        for i, task in enumerate(sorted_tasks):
            print(f"{i+1}. {task}")
        print()

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].completed = True
            print("Task marked as completed.\n")
        else:
            print("Invalid task number.\n")

# --- Driver Code ---
def main():
    manager = TaskManager()
    while True:
        print("==== Task Menu ====")
        print("1. Add Task")
        print("2. Show All Tasks")
        print("3. Complete Task")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == '1':
            title = input("Enter task title: ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            priority = input("Priority (1 = High, 2 = Medium, 3 = Low): ")
            manager.add_task(title, deadline, priority)

        elif choice == '2':
            manager.show_tasks()

        elif choice == '3':
            manager.show_tasks()
            num = int(input("Enter task number to complete: "))
            manager.complete_task(num)

        elif choice == '4':
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
