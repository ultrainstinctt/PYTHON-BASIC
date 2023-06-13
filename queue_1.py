l=[]
while True:
    a=int(input('''
            1.PUSH 
            2.POP
            3.FRONT
            4.REAR
            5.DISPLAY
            6.EXIT
            '''))
    if a==1:
        n=input("Enter a Value: ")
        l.append(n)
        print(l)


    elif a==2:
        if len(l)==0:
            print("empty queue")
        else:
            print("privious list:",l)
            del l[0]
           
            print("after pop: ",l)

    elif a==3:
        if len(l)==0:
            print("empty queue")
        else:
            print("FIRST queue valid",l[0])
    elif a==4:
       if len(l)==0:
            print("empty queue")
       else:
            print("LAST queue valid",l[-1])
    elif a==5:
    
            print("display queue",l)
    elif a==6:
        break
    else:
        print("invalid")