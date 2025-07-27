def todo():
    tasks = []

    while(True):
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task : ")
            tasks.append(task)
            print(f"Task '{task}' added.")
            
        elif choice == '2':
            if not tasks:
                print("No tasks to remove.")
                continue

            print("Current tasks:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
            
            try:
                
                task_num = int(input("Enter the task number to remove: "))
                
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '3':
            print("\n--- Your Tasks ---")
            if not tasks:
                print("Your to-do list is empty.")
            else:
                for i, task in enumerate(tasks):
                    print(f"{i + 1}. {task}")
                print('\n')  
        elif choice == '4':
            print("Exiting the to-do list.")
            break
            
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

todo()