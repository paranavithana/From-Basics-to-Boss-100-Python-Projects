#2025.04.28 ---> Matheesha Paranavithana
from datetime import datetime
from datetime import date
import calendar

print("Let's Calculate your expences....")
print()
print("1. Add a new expences")
print("2. View all expences")
print("3. Show total expences today")
print("4. Show total expences monthly")
print("5. Exit")
print()
add=input("Choose----> ")

lst=[]
f1=open("Project6.txt","a")

if add=="1":
    print()
    print("Add a new expences....")
    for i in range(1000000):
        dt=input("Enter the date (YYYY.MM.DD)---> ")
        try:
            datetime.strptime(dt, "%Y.%m.%d")
            lst.append(dt)
            print()
            break
        except:
            print("Invalied! Enter Date...")
            print()
            continue

    for i in range(1000000):
        spend=input("Enter how much rupees you spend---> Rs.")
        try:
            inspend=int(spend)
            lst.append(inspend)
            print()
            break
        except ValueError:
            print("Invalied! Enter the expences...")
            print()
            continue
        
    for i in range(1000000):
        typ=input("Enter food, travel or etc---> ")
        try:
            intyp=int(typ)
            print("Invalied!")
            print()
            continue
        except ValueError:
            lst.append(typ.lower())
            print()
            break

    for i in range(3):
        w=lst.pop(0)
        try:
            f1.write(w)
            f1.write(",")
        except TypeError:
            u=str(w)
            f1.write(u)
            f1.write(",")

    f1.write("\n")    
    f1.close()       
    f2=open("Project6.txt")
    f1.close()

elif add=="2":
    x=int(0)
    y=[]
    print()
    f1=open("Project6.txt")
    print("+---------------------+------------------------+----------------------------+")
    print("|  Date               |   Price (Rs)           |   Type                     |")
    print("+---------------------+------------------------+----------------------------+")
    for line in f1:
        clean=line.split(",")
        print("+",clean[0],"         +",clean[1]," "*(21-len(clean[1])),"+",clean[2]," "*(25-len(clean[2])),"+")
        print("+---------------------+------------------------+----------------------------+")
        x=x+int(clean[1])
        y.append(x)
    print("+", "Total"," "*40,"Rs",x," "*(22-len(str(y[0]))),"+")
    print("+---------------------+------------------------+----------------------------+")
    #this table thing is amazing, I can't even believe I build this crazy.. :)

elif add=="3":
    print()
    x=int(0)
    y=[]
    f1=open("Project6.txt")
    today=date.today()
    formatt=today.strftime("%Y.%m.%d")
    print("Today's expencess",today)
    print()
    print("+------------------------+----------------------------+")
    print("|   Price (Rs)           |   Type                     |")
    print("+------------------------+----------------------------+")
    for line in f1:
        clean=line.split(",")
        if clean[0]==formatt:
            print("+",clean[1]," "*(21-len(clean[1])),"+",clean[2]," "*(25-len(clean[2])),"+")
            print("+------------------------+----------------------------+")
            x=x+int(clean[1])
            y.append(x)     
        else:
            print()
            print("No! expences today...")
            break
        print("+", "Total"," "*30,"Rs",x," "*(9-len(str(y[0]))),"+")
        print("+------------------------+----------------------------+")
         
elif add=="4":
    print()
    h=[]
    test=[]
    f1=open("Project6.txt")
    for line in f1:
        clean=line.split(",")
        year=clean[0].split(".")
        month=year[1]
        h.append(month)
    f1.close()    
    h=list(dict.fromkeys(h))
    
    for i in h:
        x=int(0)
        y=[]
        f2=open("Project6.txt")
        g=int(i)
        month_name=calendar.month_name[g]
        print("This is expences of--->",month_name)
        print("+------------------------+----------------------------+")
        print("|   Price (Rs)           |   Type                     |")
        print("+------------------------+----------------------------+")
        for line in f2:
            clean=line.split(",")
            year=clean[0].split(".")
            month=year[1]
            if i==month:
                print("+",clean[1]," "*(21-len(clean[1])),"+",clean[2]," "*(25-len(clean[2])),"+")
                print("+------------------------+----------------------------+") 
                x=x+int(clean[1])
                y.append(x)
            else:
                continue

        print("+", "Total"," "*31,"Rs",x," "*(9-len(str(y[0]))),"+")
        print("+------------------------+----------------------------+")    
        print()
        print()

else:
    print("Bye...")
    exit()
