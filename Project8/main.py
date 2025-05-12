#2025.05.11 ---> Matheesha Paranavithana
from datetime import datetime
from datetime import date

print("Task manager...")
while True:
    print("1. Add new task")
    print("2. View all tasks")
    print("3. more")
    print("4. Exit")
    print()
    no=input("chooce----> ")
    print()
    a=["high","medium","low"]
    
    if no=="1":
        f1=open("project8.txt","a")
        name=input("Name of the task---->")
        f1.write(name)
        f1.write(",")
        while True:
            level=input("Enter priority level (High/Medium/Low) ---->")
            level=level.lower()
            if level in a:
                f1.write(level)
                f1.write(",")
                break
            else:
                continue  
        for i in range(1000000):
            r=date.today()
            dt=input("Enter the date (YYYY.MM.DD)---> ")
            try:
                datetime.strptime(dt, "%Y.%m.%d")
                f1.write(dt)
                f1.write(",")
                f1.write("\n")
                print()
                break
            except:
                print("Invalied! Enter Date...")
                print()
                continue
        f1.close()

    elif no=="2":
        low=[]
        with open("project8.txt") as f1:
            print("High priority....")
            print("+---------------------------+--------------------------+-----------------------------+")
            print("|        Name               +       Deadline           +       Status                +")
            print("+---------------------------+--------------------------+-----------------------------+")
            for line in f1:
                u=line.strip().split(",")
                if len(u)>1:
                    if u[1]=="high":
                        status = "Done" if len(u) > 3 and u[3].strip() == "done" else ""
                        print("+",u[0]," "*(24-len(u[0])),"+",u[2]," "*(23-len(u[2])),"+",status," "*(26-len(status)),"+")
                        print("+---------------------------+--------------------------+-----------------------------+")
                else:
                    continue
            print()
            f1.close()

        with open("project8.txt") as f1:
            print("Medium priority....")
            print("+---------------------------+--------------------------+-----------------------------+")
            print("|        Name               +       Deadline           +       Status                +")
            print("+---------------------------+--------------------------+-----------------------------+")
            for line in f1:
                u=line.strip().split(",")
                if len(u)>1:
                    if u[1]=="medium":
                        status = "Done" if len(u) > 3 and u[3].strip() == "done" else ""
                        print("+",u[0]," "*(24-len(u[0])),"+",u[2]," "*(23-len(u[2])),"+",status," "*(26-len(status)),"+")
                        print("+---------------------------+--------------------------+-----------------------------+") 
                else:
                    continue
            print()
            f1.close()

        with open("project8.txt") as f1:
            print("Low priority....")
            print("+---------------------------+--------------------------+-----------------------------+")
            print("|        Name               +       Deadline           +       Status                +")
            print("+---------------------------+--------------------------+-----------------------------+")
            for line in f1:
                u=line.strip().split(",")
                if len(u)>1:
                    if u[1]=="low":
                        status = "Done" if len(u) > 3 and u[3].strip() == "done" else ""
                        print("+",u[0]," "*(24-len(u[0])),"+",u[2]," "*(23-len(u[2])),"+",status," "*(26-len(status)),"+")
                        print("+---------------------------+--------------------------+-----------------------------+")
                else:
                    continue
            print()
            f1.close()

    elif no == "3":
        test = []
        print("1. Mark as done")
        print("2. Delete a Task")
        print("3. Back")
        print()
    
        choice = input("chooce----> ")
        if choice == "1":
            with open("project8.txt", "r") as f1:
                for line in f1:
                    while True:
                        print(line.strip())
                        print("Enter 'done' or hit 'enter' to skip")
                        a = input("---> ")

                        if a.lower() == "done":
                            updated_line = line.strip() + "done,\n"
                            test.append(updated_line)
                            print()
                            break
                        elif a == "":
                            print("Skipped...")
                            print()
                            test.append(line)
                            break
                        else:
                            print("Invalid")
                            print()
                            continue

            with open("project8.txt", "w") as f2:
                f2.writelines(test)
            f2.close()
            
        elif choice=="2":
            updated_lines = []
            with open("project8.txt", "r") as f:
                for line in f:
                    print(line.strip())
                    de=input("Enter 'del' to delete or 'enter' to skip....")
                    print()
                    if de.lower()=="del":
                        continue
                    elif de=="":
                        updated_lines.append(line)

            with open("project8.txt", "w") as f:
                f.writelines(updated_lines)

        elif choice=="3":
            break
        else:
            print("Invalied")
            break



          
