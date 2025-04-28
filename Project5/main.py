import random

print("Let's do some quez....")
user=int(input("Enter how much quez u need---> "))
print()
f1=open("data2.txt")
lst=[]
test=[]

for i in f1:
    w=i.strip()
    lst.append(w)
    
if len(lst)>=user:
    for lst in random.sample(lst,user):
        test.append(lst)
    for h in range(user):
        k=test.pop(0).strip("[").strip("]").split(",")
        r=input(k[0])
        g=k[1].strip()
        if r.lower()==g:
            print("correct...")
            print()
        else:
            print("wrong...",g)
            print()
        
else:
    for lst in random.sample(lst,len(lst)):
        test.append(lst)    
    print("There not much quiz there....")
    print()
    for h in test:
        k=h.strip("[").strip("]").split(",")
        r=input(k[0])
        g=k[1].strip()
        if r.lower()==g:
            print("correct...")
            print()
        else:
            print("wrong...",g)
            print()
print()
