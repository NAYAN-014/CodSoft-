def task():
    tasks = []
    print("task management app")
    
    alltask = int(input("Enter how many task you want to add ="))
    for i in range(1, alltask+1):
        task_name = input(f"enter task {i}=")
        tasks.append(task_name)

    print(f"Today task are\n{tasks}")

    while True:
        print("choose operation")
        print("1.Add task ")
        print("2.Update task ")
        print("3.View task")
        print("4.Delete task")
        print("5.Exit task ")
        print("")

        operation =int(input("choose operation between 1-5="))
        if operation==1:
            add=input("Enter task you want to add= ")
            tasks.append(add)
            print(f"Task {add} has been added.")

        elif operation==2:
            update= input("Enter new task name you want to update=")
            if update in tasks:
                up=input("Enter new task=")
                ind=tasks.index(update)
                tasks[ind]=up
                print(f"updated task {up}")

        elif operation==3:
            print(f"Total task ={tasks}")  

        elif operation==4:
            del_val =input("Enter the task name you want to delete=")
            if del_val in tasks:
                ind = tasks.index(del_val)   
                del tasks[ind]
                print(f"Task {del_val} has been deleted.")   

        elif operation==5:
            print("closing the program.")
            break

        else:
            print("*invalid input*")

task()

