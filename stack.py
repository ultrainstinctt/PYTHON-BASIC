l=[]
while True:
    a=int(input('''
            1.PUSH 
            2.POP
            3.PEEK
            4.DISPLAY
            5.EXIT
            '''))
    if a==1:
        n=input("Enter a Value: ")
        l.append(n)
        print(l)


    elif a==2:
        if len(l)==0:
            print("empty stack")
        p=l.pop()
        print(p)
        print(l)
    elif a==3:
        if len(l)==0:
            print("empty stack")
        else:
            print("last stack valid",l[-1])
    elif a==4:
        print("display stach",l)
    elif a==5:
        break
    else:
        print("invalid")