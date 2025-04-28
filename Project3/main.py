import random
print("Wanna some maths quiz")
r=[2]
i=len(r)
while 2-i==1:
    try:
        w=input("Enter, how much quiz do u need.... ")
        d=int(w)
        r.append(d)
        break
        
    except ValueError:
        print("Enter correct stuff")
    print()
print()

u=r[1]
o=int(u)
for i in range(o):
    u=random.randint(1,100)
    v=random.randint(1,100) 
    item=("+","-","*","/")
    t=random.choice(item)
    
    if t=="+":
        f=print(u,"+",v)
        e=float(input())
        r=u+v      
        try:
            if e==r:
                print("Correct")
            else:
                print("wrong, answer is",u+v)
                
        except ValueError:
            print("Enter correct stuff...")
        print()    

    elif t=="-":
        f=print(u,"-",v)
        e=float(input())
        r=u-v      
        try:
            if e==r:
                print("Correct")
            else:
                print("wrong, answer is",u-v)
                
        except ValueError:
            print("Enter correct stuff...")
        print()
        
    elif t=="*":
        ui=random.randrange(20)
        f=print(u,"*",ui)
        e=float(input())
        r=u*ui      
        try:
            if e==r:
                print("Correct")
            else:
                print("wrong, answer is",u*ui)
                
        except ValueError:
            print("Enter correct stuff...")
        print()
        
    elif t=="/":
        ui=random.randrange(20)
        f=print(u,"/",ui)
        e=float(input())
        r=u/ui
        yo=int(r*100)/100
        try:
            if e==yo:
                print("Correct")
            else:
                print("wrong, answer is",yo)
                
        except ValueError:
            print("Enter correct stuff...")
        print()    
    else:
        print("invalied")
        print()
