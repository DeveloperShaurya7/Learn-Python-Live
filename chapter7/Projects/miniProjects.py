taskList = [] # Task list

while True:
    print("\n-------------- To Do List ------------")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":  #if user enters choice 1 for entering task
        task = input("Enter Task: ")
        taskList.append(task)
        print("Task Added")

    elif choice == "2":  #if user enters choice 1 for entering task
        task = input("Enter task to Remove: ")
        if task in taskList:
            taskList.remove(task)
            print("Task removed")
        else:
            print("Task not found")

    elif choice == "3":  #if user enters choice 1 for entering task
        task = print("\n Your Tasks: ") #\n - It creates new line
        for t in taskList:
            print("-", t)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
            




