class Task:
    def __init__(self, taskId, taskName, status):
        self.taskId = taskId
        self.taskName = taskName
        self.status = status

    def __str__(self):
        return f"[{self.taskId}] {self.taskName} - {self.status}"

class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

class TaskManager:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = Node(task)
        new_node.next = self.head
        self.head = new_node

    def search_task(self, task_id):
        current = self.head
        while current:
            if current.task.taskId == task_id:
                return current.task
            current = current.next
        return None

    def delete_task(self, task_id):
        current = self.head
        prev = None
        while current:
            if current.task.taskId == task_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def traverse_tasks(self):
        if not self.head:
            print("No tasks available.")
        else:
            current = self.head
            while current:
                print(current.task)
                current = current.next

# 🔁 CLI Loop
def main():
    tm = TaskManager()
    while True:
        print("\n--- Task Management System ---")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Search Task by ID")
        print("4. Delete Task by ID")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            taskId = int(input("Enter Task ID: "))
            taskName = input("Enter Task Name: ")
            status = input("Enter Status (Pending/In Progress/Completed): ")
            tm.add_task(Task(taskId, taskName, status))
            print("✅ Task added.")

        elif choice == "2":
            print("\n📋 All Tasks:")
            tm.traverse_tasks()

        elif choice == "3":
            taskId = int(input("Enter Task ID to search: "))
            task = tm.search_task(taskId)
            print(task if task else "❌ Task not found.")

        elif choice == "4":
            taskId = int(input("Enter Task ID to delete: "))
            deleted = tm.delete_task(taskId)
            print("🗑️ Task deleted." if deleted else "❌ Task not found.")

        elif choice == "5":
            print("👋 Exiting. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
