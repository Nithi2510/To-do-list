print("Welcome to the To-Do List App!")

tasks = []

while True:
    print("\nMenu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Edit Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        if len(tasks) == 0:
            print("No tasks to show.")
        else:
            print("\nTo-Do List:")
            for i in range(len(tasks)):
                status = "✔" if tasks[i]['completed'] else "✘"
                print(f"{i + 1}. [{status}] {tasks[i]['task']}")
    
    elif choice == '2':
        new_task = input("Enter the task: ")
        task_item = {
            'task': new_task,
            'completed': False
        }
        tasks.append(task_item)
        print("Task added successfully.")

    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to mark as complete.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]['task']}")

            index = int(input("Enter the task number to mark as complete: ")) - 1
            if index >= 0 and index < len(tasks):
                tasks[index]['completed'] = True
                print("Task marked as complete.")
            else:
                print("Invalid task number.")
    
    elif choice == '4':
        if len(tasks) == 0:
            print("No tasks to edit.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]['task']}")

            index = int(input("Enter the task number to edit: ")) - 1
            if index >= 0 and index < len(tasks):
                new_text = input("Enter the new task description: ")
                tasks[index]['task'] = new_text
                print("Task updated successfully.")
            else:
                print("Invalid task number.")
    
    elif choice == '5':
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]['task']}")

            index = int(input("Enter the task number to delete: ")) - 1
            if index >= 0 and index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"Task '{removed_task['task']}' deleted successfully.")
            else:
                print("Invalid task number.")
    
    elif choice == '6':
        print("Exiting the To-Do List App. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
