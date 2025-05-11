#2025.05.06
from datetime import date
from datetime import datetime

while True:
    print("Daily Journal App....")
    print("1. Enter New Entry")
    print("2. Search by Date")
    print("3. View all Entries")
    print("4. Exit")
    print()
    day=input("Choice--->")
    a=1
    f4=open("datesdata.txt","a")
    if day=="1":
        
        today=date.today()
        todayw=today.strftime("%Y.%m.%d")
        file_name=f"{todayw}_entry.txt"
        f4.write(file_name)
        f4.write("\n") 
        x=1
        
        try:
            f1=open(file_name,"r")
        except FileNotFoundError:
            f1=open(file_name,"x")
        for line in f1:
            x=x+1
            
        for i in range(x,11):
            if i==10:
                print("Daily entries over... :(")
                break
            f2=open(file_name,"a") 
            print(today,"Enter Today Entry",i,"/10")
            entry=input("What is happend now---> ")
            mode=input("What is your mode now---> ")
            ex=input("Enter 'exit' to stop or 'more' to continue---> ")
            f2.write(entry)
            f2.write(",")
            f2.write(mode)
            f2.write(",")
            f2.write("\n")
            f2.close()
            print()
            if ex.lower()=="exit":
                break
            elif ex.lower()=="more":
                continue
            continue
        print()

    elif day == "2":
        with open("datesdata.txt") as f5:
            date_input = input("Enter the date (YYYY.MM.DD)---> ")
            print()
            found = False
            for i in f5:
                t = i.strip().removesuffix("_entry.txt")
                if t == date_input:
                    r=i.strip()
                    f1=open(r)
                    print("+--------------------------------------------------------------------+-----------------+")
                    print("| Notes"," "*60,"| Mode"," "*10,"|") 
                    for j in f1:
                        w=j.split(",")
                        print("+--------------------------------------------------------------------+-----------------+")
                        print("+",w[0]," "*(65-len(w[0])),"+",w[1]," "*(14-len(w[1])),"+")
                    print("+--------------------------------------------------------------------+-----------------+")    
                    f1.close()
                    found = True
        if not found:
            print("No entry found for that date.")


    elif day=="3":
        with open("datesdata.txt") as f5:
            for i in f5:
                y=i.strip().removesuffix("_entry.txt")
                print(y)
                t = i.strip().removesuffix("_entry.txt")
                r=i.strip()
                f1=open(r)
                print("+--------------------------------------------------------------------+-----------------+")
                print("| Notes"," "*60,"| Mode"," "*10,"|") 
                for j in f1:
                    w=j.split(",")
                    print("+--------------------------------------------------------------------+-----------------+")
                    print("+",w[0]," "*(65-len(w[0])),"+",w[1]," "*(14-len(w[1])),"+")
                print("+--------------------------------------------------------------------+-----------------+")
                print()
                f1.close()

    elif day=="4":
        exit("Good day...")
        
    else:
        print("Invalied... :(")
        print()
        
