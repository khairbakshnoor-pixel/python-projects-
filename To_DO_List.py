tasks = []

print("Welcome to the TASK MANAGEMENT APP")

total_task = int(input("Enter the total number of tasks: "))

for i in range(1, total_task + 1):
    task_name = input(f"Enter task {i}: ")
    tasks.append(task_name)

print("Today's tasks are:")
for task in tasks:
    print("-", task)

while True:
    print("\n1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. View Tasks")
    print("5. Exit")

    op = int(input("Choose an option: "))

    if op == 1:
        add = input("Enter new task: ")
        tasks.append(add)
        print(f"Task '{add}' added successfully")

    elif op == 2:
        update = input("Enter task name to update: ")
        if update in tasks:
            new_task = input("Enter new task name: ")
            index = tasks.index(update)
            tasks[index] = new_task
            print("Task updated successfully")
        else:
            print("Task not found")

    elif op == 3:
        delete = input("Enter task name to delete: ")
        if delete in tasks:
            tasks.remove(delete)
            print("Task deleted successfully")
        else:
            print("Task not found")

    elif op == 4:
        print("Your tasks:")
        for task in tasks:
            print("-", task)

    elif op == 5:
        print("Exiting Task Manager. Goodbye!")
        break

    else:
        print("Invalid option, try again")
