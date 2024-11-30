def task():
    tasks = [ ]
    print("Welcome to To Do list")

    total_task = int(input("Enter the number of task you want to do : "))
    for i in range(1,total_task+1):
        task_name = input(f"Enter the {i} = ")
        tasks.append(task_name)
    print(f"Task for toady are : \n {tasks}")
    while True:
        operation = int(input("\n Enter 1 : Add \n Enter 2 : Update \n Enter 3: Delete \n Enter 4: View \n Enter 5: Exit  :"))
        if operation == 1:
            add = input("Enter the task you want to add :")
            tasks.append(add)
            print(f"task {add} has been successfully added.")
        elif operation == 2:
            update_val = input("Enter the task you want to update :")
            if update_val in tasks:
                np = input("Enter new task. ")
                ind = tasks.index(update_val)
                tasks[ind] = np
                print(f"task {np} has been successfully updated.")
        elif operation == 3:
            delete_val = input("Enter the task you want to delete :")
            if delete_val in tasks:
                ind = tasks.index(delete_val)
                del tasks[ind]
                print(f"task {delete_val} has been successfully deleted.")
        elif operation == 4:
            print(f"Total task = {tasks}")
        elif operation == 5:
            print("Thank You")
            break
        else:
            print("Invalid input")

task()


