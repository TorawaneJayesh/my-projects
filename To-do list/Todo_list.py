# this is my todo list project. 

def view_tasks():
    try:
        with open("Todo.txt","r") as f:
            tasks = f.read()
            print(tasks)
    except FileNotFoundError:
        print("tasks is empty")
        
        
def add_tasks():
    with open("Todo.txt","a") as f:
        t1 = input("enter task for add...")
        f.write("\n"+t1)
        print(f"task added...{t1}")

def delete_task():
    with open("Todo.txt","r") as f:
        tasks = f.readlines()
        print(tasks,"\n")
    deletetask = input("enter the task which need to delete.")
    with open("Todo.txt","w") as f:
        for task in tasks:
            if task.strip() != deletetask:
                f.write(task)
        print(f"{deletetask} task has been deleted...")

while True:
    uc = input("1) View Task \n2) Add Task \n3) Delete Task \nexit) Close App: ")
    if uc == '1':
        view_tasks()
        print("this are your tasks...")
    elif uc == '2':
        add_tasks()
    elif uc == '3':
        delete_task()
    elif uc == 'exit':
        print("you are exit!")
        break
    else:
        print("invalid choice please enter valid credential!")
