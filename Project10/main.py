#2025.05.29---->Matheesha Paranavithana
from datetime import datetime
import random
import string

print("Password strength analyzer...")
while True:
    print("1. Cheak Password strength") #weak, moderate, strong---based on length, numbers, Arithmetic symbols
    print("2. Generate strong password")
    print("3. View log")
    print("4. Clear log")
    print("5. Exit Program")
    print()
    no=input("Choice---->")
    print()
    if no=="1":
        with open("data10.txt","a") as f1:
            x=0
            a=["!","@","#","$","%","^","&","*","(",")","_","+","{","}",":","|","<",">","?","~","`",",",".","/",";","[","]","-","="]
            enter=input("Enter your password---->")
            enterl=list(str(enter))
            test=[]
            f1.write(enter)
            f1.write(",")
         
            for i in a:
                for j in enterl:
                    if i==j:
                        x=x+1
        
            y=len(enterl)
            q=0
            for i in enterl:
                try:
                    no=int(i)
                    q=q+1
                except ValueError:
                    test.append(i)
                    continue
            
            lowercase=0
            uppercase=0
            for i in enterl:
                if i==i.lower():
                    try:
                        no=int(i)
                        continue
                    except ValueError:
                        lowercase+=1
                else:
                    try:
                        no=int(i)
                        continue
                    except ValueError:
                        uppercase+=1             

            if y>=8:
                if x>0:
                    if q>0:
                        if lowercase!=len(test):
                            print("Strong")
                            f1.write("Strong")
                            f1.write(",")
                            print()
                        else:
                            print("Moderate use mixsure of capital and simple letters")
                            print()
                            f1.write("Moderate use mixsure of capital and simple letters")
                            f1.write(",")
                    elif lowercase!=len(test):
                        print("Strong")
                        print()
                        f1.write("Strong")
                        f1.write(",")
                    else:
                        print("Moderate use some numbers and capital and simple letters")
                        print()
                        f1.write("Moderate use some numbers and capital and simple letters")
                        f1.write(",")
                elif q>0:
                    if lowercase!=int(len(test)):
                        print("Moderate use some arithmetic symbols and capital and simple letters")
                        print()
                        f1.write("Moderate use some arithmetic symbols and capital and simple letters")
                        f1.write(",")
                        
                    elif lowercase==int(len(test)):
                        print("Moderate use Arithmetic symbols and capital and simple letters")
                        print()
                        f1.write("Moderate use Arithmetic symbols and capital and simple letters")
                        f1.write(",")
                    else:
                        print("Weak use Arithmetic symbols number capital and simple letters")
                        print()
                        f1.write("Weak use Arithmetic symbols number capital and simple letters")
                        f1.write(",")
            else:
                print("Weak enter more than 8 characters")
                print()
                f1.write("Weak enter more than 8 characters")
                f1.write(",")

            today=datetime.today()
            f1.write(str(today))
            f1.write(",")
            f1.write("\n")

    elif no=="2":
        x=""
        for i in range(20):
            a=["!","@","#","$","%","^","&","*","(",")","_","+","{","}",":","|","<",">","?","~","`",",",".","/",";","[","]","-","="]
            test=random.choice(a)
            rand_str=random.choice(string.ascii_letters)
            no=random.randint(0,9)
            y=[test,rand_str,no]
            x=x+str(random.choice(y))
            u=[]

            if y==rand_str:
                u.append(y)
                

            if len(x)==10:
                if x in a:
                    if x in no:
                        if x in u.pop(0):
                            break
                break
            else:
                continue
        print(x)
        print()
                    

        
            
    elif no=="3":
        with open("data10.txt","r") as f1:
            for i in f1:
                print(i)

    elif no=="4":
        f1=open("data10.txt","w")
        print("Log cleared.... :)")
        print()

    elif no=="5":
        print("ended.... :(")
        break

    else:
        print("Invalied.... :(")


                                                                                                                                                                                                                                                                                                                           
