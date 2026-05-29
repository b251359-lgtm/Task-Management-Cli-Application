import sqlite3
from datetime import datetime


class TaskManager:
    def __init__(self):
        self.connection = sqlite3.connect("tasks.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    # Create tasks table
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            deadline TEXT,
            status TEXT
        )
        '''

        self.cursor.execute(query)
        self.connection.commit()

    # Add new task
    def add_task(self):
        print("\n========== ADD TASK ==========")

        title = input("Enter task title: ")
        description = input("Enter task description: ")
        deadline = input("Enter deadline (YYYY-MM-DD): ")

        status = "Pending"

        query = '''
        INSERT INTO tasks (title, description, deadline, status)
        VALUES (?, ?, ?, ?)
        '''

        self.cursor.execute(query, (title, description, deadline, status))
        self.connection.commit()

        print("\nTask added successfully!")

    # View all tasks
    def view_tasks(self):
        print("\n========== ALL TASKS ==========")

        query = "SELECT * FROM tasks"
        self.cursor.execute(query)

        tasks = self.cursor.fetchall()

        if not tasks:
            print("\nNo tasks found!")
            return

        for task in tasks:
            print(f"\nTask ID      : {task[0]}")
            print(f"Title        : {task[1]}")
            print(f"Description  : {task[2]}")
            print(f"Deadline     : {task[3]}")
            print(f"Status       : {task[4]}")
            print("------------------------------------")

    # Update task status
    def update_task(self):
        print("\n========== UPDATE TASK ==========")

        task_id = input("Enter Task ID: ")

        print("1. Pending")
        print("2. Completed")

        choice = input("Choose status: ")

        if choice == '1':
            status = "Pending"
        elif choice == '2':
            status = "Completed"
        else:
            print("Invalid choice!")
            return

        query = "UPDATE tasks SET status = ? WHERE id = ?"

        self.cursor.execute(query, (status, task_id))
        self.connection.commit()

        print("\nTask updated successfully!")

    # Delete task
    def delete_task(self):
        print("\n========== DELETE TASK ==========")

        task_id = input("Enter Task ID to delete: ")

        query = "DELETE FROM tasks WHERE id = ?"

        self.cursor.execute(query, (task_id,))
        self.connection.commit()

        print("\nTask deleted successfully!")

    # Filter tasks by status
    def filter_tasks(self):
        print("\n========== FILTER TASKS ==========")

        print("1. Pending Tasks")
        print("2. Completed Tasks")

        choice = input("Choose option: ")

        if choice == '1':
            status = "Pending"
        elif choice == '2':
            status = "Completed"
        else:
            print("Invalid choice!")
            return

        query = "SELECT * FROM tasks WHERE status = ?"

        self.cursor.execute(query, (status,))

        tasks = self.cursor.fetchall()

        if not tasks:
            print(f"\nNo {status.lower()} tasks found!")
            return

        for task in tasks:
            print(f"\nTask ID      : {task[0]}")
            print(f"Title        : {task[1]}")
            print(f"Description  : {task[2]}")
            print(f"Deadline     : {task[3]}")
            print(f"Status       : {task[4]}")
            print("------------------------------------")

    # Close database connection
    def close_connection(self):
        self.connection.close()


# Display menu

def display_menu():
    print("\n========== TASK MANAGEMENT SYSTEM ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Filter Tasks")
    print("6. Exit")


# Main Program

def main():
    manager = TaskManager()

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == '1':
            manager.add_task()

        elif choice == '2':
            manager.view_tasks()

        elif choice == '3':
            manager.update_task()

        elif choice == '4':
            manager.delete_task()

        elif choice == '5':
            manager.filter_tasks()

        elif choice == '6':
            manager.close_connection()
            print("\nExiting Task Manager...")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()
