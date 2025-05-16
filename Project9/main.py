#2025.05.14 --->Matheesha Paranavithana

print("Contact Book....")
while True:
    print()
    print("1. Add contact")
    print("2. Search contact")
    print("3. View all contact")
    print("4. Update contact info")
    print("5. Delete contact")
    print("6. Exit Program")
    print()
    no=input("Choice----> ")

    if no=="1":
        with open("project9.txt","a") as f1:
            name=input("Enter Name----> ")
            f1.write(name.lower())
            f1.write(",")
            while True:
                number=input("Enter phone number----> ")
                try:
                    test=int(number)
                    f1.write(number)
                    f1.write(",")
                    break
                except ValueError:
                    print("Invalied.... :( ")
                    print()
                    continue
                break       
            email=input("Enter email address----> ")
            f1.write(email)
            f1.write(",\n")
            print("Done...")
            continue
        
    elif no=="2":
        with open("project9.txt","r") as f1:
            print("1. Search by number")
            print("2. Search by name")
            print()
            user=input("choice----> ")
            print()
            for i in f1:
                if user=="1":
                    while True:
                        t=input("Enter phone number----> ")
                        i=i.strip().split(",")
                        if t==i[1]:
                            print("Name   - ",i[0])
                            print("Number - ",i[1])
                            print("Email  - ",i[2])
                            print()
                            break
                        else:
                            print("404 .... :( ")
                            continue

                elif user=="2":
                    while True:
                        t=input("Enter your name----> ")
                        i=i.strip().split(",")
                        if t.lower()==i[0]:
                            print("Name   - ",i[0])
                            print("Number - ",i[1])
                            print("Email  - ",i[2])
                            print()
                            break
                        else:
                            print("404 .... :( ")
                            continue
                else:
                    print("Invalied.... :( ")
                    print()
                    break
                        
    elif no=="3":
        with open("project9.txt","r") as f1:
            print("+---------------------------------+-------------------------------+----------------- ---------------------------+")
            print("+          Name                   +          Number               +                     Email                   +")
            print("+---------------------------------+-------------------------------+---------------------------------------------+")
            for i in f1:
                i=i.strip().split(",")
                print("+",i[0]," "*(30-len(i[0])),"+",i[1]," "*(28-len(i[1])),"+",i[2]," "*(42-len(i[2])),"+")
                print("+---------------------------------+-------------------------------+---------------------------------------------+")

    elif no=="4":
        test=[]
        with open("project9.txt","r") as f1:
            
            for i in f1:
                l=i.strip().split(",")
                print("Update---",l[0],"to")
                name=input("Add New Name or 'Enter' to skip---->")
                no=input("Add New Phone Number or 'Enter' to skip---->")
                email=input("Add New Email or 'Enter' to skip---->")
                
                if name=="":
                    if len(no)>0:
                        if len(email)>0:
                            h=str(l[0])+","
                            test.append(h)
                            y=no+","
                            test.append(y)
                            x=email+",\n"
                            test.append(x)
                            print()

                        else:
                            h=str(l[0])+","
                            test.append(h)
                            y=no+","
                            test.append(y)
                            x=str(l[2].strip(","))+",\n"
                            test.append(x)
                            print()
                    else:
                        if len(email)>0:
                            h=str(l[0])+","
                            test.append(h)
                            y=str(l[1])+","
                            test.append(y)
                            x=email+",\n"
                            test.append(x)
                            print()
                        else:
                            h=str(l[0])+","
                            test.append(h)
                            y=str(l[1])+","
                            test.append(y)
                            x=str(l[2])+",\n"
                            test.append(x)
                            print()
  
                elif len(name)>0:  
                    if len(no)>0:
                        if len(email)>0:
                            h=name+","
                            test.append(h)
                            y=no+","
                            test.append(y)
                            x=email+",\n"
                            test.append(x)
                            print()

                        else:
                            h=name+","
                            test.append(h)
                            y=no+","
                            test.append(y)
                            x=str(l[2].strip(","))+",\n"
                            test.append(x)
                            print()
                    else:
                        if len(email)>0:
                            h=name+","
                            test.append(h)
                            y=str(l[1])+","
                            test.append(y)
                            x=email+",\n"
                            test.append(x)
                            print()
                        else:
                            h=name+","
                            test.append(h)
                            y=str(l[1])+","
                            test.append(y)
                            x=str(l[2])+",\n"
                            test.append(x)
                            print()                       
                    
        with open("project9.txt","w") as f1:
            f1.writelines(test)


    elif no=="5":
        updated_lines = []
            with open("project9.txt", "r") as f:
                for line in f:
                    print(line.strip())
                    de=input("Enter 'del' to delete or 'enter' to skip....")
                    print()
                    if de.lower()=="del":
                        continue
                    elif de=="":
                        updated_lines.append(line)

            with open("project9.txt", "w") as f:
                f.writelines(updated_lines)

    elif no=="6":
        exit()

    else:
        print("Invalied....")
                
                    
            
