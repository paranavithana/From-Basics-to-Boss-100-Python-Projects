print("Lets Calculate.....")
print("Enter your Calculations like (12+5)")
print("'history' to watch previous calculations")
a=[]
h=[]

while 1<2:
    
    
    e=input("'end' to stop- ")
    if e.lower()=="end":
        print("Ended")
        q=len(a)
        for i in range(q):
            b="".join(a.pop(0))
            k=eval(b)
            print(b ,"=", k)
            u=f"{b}={k}"
            h.append(u)
  
    
    elif e.lower()=="history":
        print(h)
        
    try:
        a.append(e)
        
    except ValueError:
        print("Enter Correct Stuff")
