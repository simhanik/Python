def task():
    tasks = []  # empty list
    print("---WELCOME TO THE TASK MANAGEMENT APP---")
    total_task = int(input("Enter how many tasks you want to add : "))  # e.g, 5
    for i in range(1, total_task+1) :   #6
        task_name = input(f"Enter task {i} : ")  # enter task 1
        tasks.append(task_name)

    print(f"Today's tasks are\n {tasks}")

    while True:
        operation = int(input("Enter following to perform more operations \n 1-Add \n 2-Update \n 3-Delete \n 4-View \n 5-Exit\n"))
        if operation == 1:
            add = input("Enter task you want to add : ")
            tasks.append(add)
            print(f"task {add} has been added successfully...")
        elif operation == 2:
            updated_val = input("Enter the task you want to update: ")
            if updated_val in tasks:
                up =input("Enter new task : ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task {up}")
        elif operation == 3:
            del_val = input("Which task you want to delete : ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted...")
        elif operation == 4:
            print(f"Total tasks : {tasks}")
        elif operation == 5:
            print("Closing the program....")
            break;
        else:
            print("Invalid Input")
        
task()
            
