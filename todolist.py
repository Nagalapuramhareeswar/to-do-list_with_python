tasks = []

def display_tasks():
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['name']} - {'Completed' if task['completed'] else 'Not Completed'}")
    else:
        print("Your to-do list is empty.")

def add_task():
    task_name = input("Enter the task's name: ")
    tasks.append({'name': task_name, 'completed': False})
    print(f"Task '{task_name}' added successfully.")

def mark_as_completed():
    display_tasks()
    task_number = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        print(f"Task '{tasks[task_number - 1]['name']}' marked as completed.")
    else:
        print("Invalid task number.")

def remove_task():
    display_tasks()
    task_number = int(input("Enter the task number to remove: "))
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['name']}' removed successfully.")
    else:
        print("Invalid task number.")


while True:
    print("\nTo-Do List Application Menu:")
    print("1. Display To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Remove a Task")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_as_completed()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Exiting the To-Do List application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
