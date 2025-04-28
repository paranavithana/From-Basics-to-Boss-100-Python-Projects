print("Let's Convert")

while True:
    print("enter '1' if you want Kilometer to Miles")
    print("enter '2' if you want Centimeter to Inches")
    print("enter '3' if you want Kilogram to Pound")
    print("want to stop enter 'end'")
    h=input(".....")
  

    if h=="1":
        print("type '1' for km--->mi")
        print("type '2' for mi--->km")
        q=input(".....")
        print()

        
        if q=="1":
            try:
                e=input("enter ur value...")
                f=float(e)
                u=f/1.609344
                print(e,"km","---->",u,"mi")
                print()
            except:
                print("Enter no only... :(")
                print()
                continue

        elif q=="2":
            try:
                e=input("enter ur value...")
                f=float(e)
                u=f/0.621371
                print(e,"mi","---->",u,"km")
                print()
            except:
                print("Enter no only... :(")
                print()
                continue  
        else:
            print("choose from menu... :(")
            continue
            print()
       
            
    elif h=="2":
        print("type '1' for cm--->in")
        print("type '2' for in--->cm")
        q=input(".....")
        print()
        if q=="1":
            try:
                e=input("enter ur value...")
                f=float(e)
                u=f*0.394
                print(e,"cm","---->",u,"in")
                print()
            except:
                print("Enter no only... :(")
                print()
                continue

        elif q=="2":
            try:
                e=input("enter ur value...")
                f=float(e)
                u=f*2.54
                print(e,"in","---->",u,"cm")
                print()
            except:
                print("Enter no only... :(")
                print()
                continue  
        else:
            print("choose from menu... :(")
            continue
            print()

            
    elif h=="3":
        print("type '1' for kg--->lbs")
        print("type '2' for lbs--->kg")
        q=input(".....")
        print()
        if q=="1":
            try:
                e=input("enter ur value...")
                f=float(e)
                u=f*2.2046
                print(e,"kg","---->",u,"lbs")
                print()
            except:
                print("Enter no only... :(")
                print()
                continue

        elif q=="2":
            try:
                e=input("enter ur value...")
                f=float(e)
                u=f*0.45359237
                print(e,"lbs","---->",u,"kg")
                print()
            except:
                print("Enter no only... :(")
                print()
                continue  
        else:
            print("choose from menu... :(")
            continue
            print()        
    else:
        print("choose from menu... :(")
        print() 
