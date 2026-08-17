tasks= []
while True:
    print("1. add a task:")
    print("2. view a tasks:")
    print("3. remove a task:")
    print("4. exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        while True:
            tasks.append(input("Enter your task:"))
            again = input("add another task, (y/N)")

            if again.lower() != "y":
                break



    elif choice == 2:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    elif choice == 3:
        if not tasks:
            print("No tasks")
        else:
            print("tasks:")
            for index,task in enumerate(tasks, start=1):
             print(f"{index}.{task}")


            task_number = int(input("Enter a number to remove:"))
            if 1<= task_number <= len(tasks):
                removed_task = tasks.pop(task_number-1)
                print(f"'{removed_task}'. removed successfully")
            else:
                print("invalid number")


    elif choice == 4:
        print("exit")
        break
    else:
        print("invalid choice")