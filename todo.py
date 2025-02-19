tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet! Add some tasks.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed = tasks.pop(task_num)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

while True:
    print("\nTo-Do List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
