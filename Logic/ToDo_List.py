todo_list=[]

while True:
    print("\n-------To Do List---------")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice=input("Enter your choice (1-4): ")
    task=0

    if choice=="1":
        print("Enter your new task: ")
        todo_list.append(task)

    elif choice=="2":    
        if len(todo_list)==0:
            print("No tasks found.")

        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")


    elif choice=="3":    
        if len(todo_list)==0:
            print("No tasks to remove.")

        else:
            task_no=int(input("Enter the task number to remove: "))
            if 1<=task_no<=len(todo_list):
                removed=todo_list.pop(task_no-1)
                print(f"Removed task: {removed}")

            else:
               print("Invalid task number")

    elif choice=="4":    
        print("GoodBye!To Do List application.")
        
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

