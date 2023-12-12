from time import sleep
task = []

while True:
    print(""""
        Welcome to your to-do-list

        What would you like to today?

        1) Add a new task
        2) Eliminate a task
        3) Complete a task 
        4) Exit 
        5) Show my to-do-lists
        
        By Ronaldo Romero Vergel 
        """)
  


    try:
        decision = int(input("Choose one option: "))
    except ValueError:
        print("Probably you wrote wrong the number, make sure that you write the number of the option that you want to execute")

    if decision == 1:
        newtask= input("what task do you want to add: ")
        task.append(newtask)  
    
    elif decision == 2:
        print(f"This is your to do list {task}")
        try: 
            del_task= int(input("what is the position of the task which you want to delete: "))
            del task[del_task]

        except IndexError:
            print("Probably you write a position that doesn't exists")
    

    elif decision == 3:
        print(f"This is your to do list {task}")
        try: 
            del_task= int(input("what is the position of the completed task: "))
            del task[del_task]

        except IndexError:
            print("Probably you write a position that doesn't exists")

    elif decision == 4:
        print("Exit...")
        break

    elif decision == 5:
        print(f"This is your to do list {task}")
    
    else:
        print("Make sure that you write correctly the option")
    
    sleep(5)
