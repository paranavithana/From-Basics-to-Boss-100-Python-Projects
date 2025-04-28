import ast
user=[]
while True:
    print("Password Vaulet")
    print("1) Add new Password")
    print("2) Watch previous saved")
    print("3) Search Website")
    print()
    try:
        use=input("chooce----> ")
        print()
        num=int(use)
        user.append(num)
        break
    except ValueError:
        print("Enter Correct Stuf")
        print()
        continue
    
x=int(user[0])
data=[]

if x==1:
    while True:
        print("Add your details...")
        name=input("1) Enter the web app name or web name---> ")
        uid=input("2) Enter user name---> ")
        psd=input("3) Enter password---> ")
        print("stored...")
        print()
        try:
            data.append(name)
            data.append(uid)
            data.append(psd)
            f1=open("data.txt","a")
            line=str(data)+"\n"
            f1.write(line)
            f1.close()
        except ValueError:
            print("Enter correct stuf")
        close=input("Enter 'end' to end--->")
        if close.lower()=="end":
            break
elif x==2:
    f2=open("data.txt")
    c=f2.read()
    print(c)
    f2.close()
    
elif x==3:
    while True:
        search=input("Enter name of the app or web or 'end' to stop---> ").strip()
        f3=open("data.txt")
        if search.lower()=="end":
            break
        for line in f3:
            try:
                u=ast.literal_eval(line)
                if str(u[0])==str(search):
                    print(u)
                    print()
                    break
                    
            except:
                continue
        
        else:
            print("Error 404: try another name...")
            print()
