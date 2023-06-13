import random
l=["rock","scissor","paper"]


while True:

    count=0
    usercount=0
    drawcount=0
    uc=(int(input('''
game start.....
1 yes.
2 no.
    ''')))



    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
            1. rock
            2. scissor
            3. paper
            
            '''))

            if userInput == 1:
                userChoice="rock"
            elif userInput ==2:
                userChoice="scissor"
            elif userInput==3:
                 userChoice="paper"
           
            choice=random.choice(l)
           
                
            #print(choice)
           # print(userChoice)
            if choice==userChoice:
                print("computer= ",choice)
                print("user= ",userChoice)
                print("game draw")
                drawcount=drawcount+1
            elif (userChoice=="rock" and choice=="scissor") or (userChoice=="paper" and choice=="rock") or(userChoice=="scissor" and choice=="paper"):
                print("you win")
                print("computer= ",choice)
                print("user= ",userChoice)
            
                usercount=usercount+1
            else:
                print("compputer win")
                print("computer= ",choice)
                print("user= ",userChoice)
                count=count+1
               

        if count==usercount:
            print("...........................................")
            print("final ans draw")
            print("user score",usercount)
            print("com score:",count)
            print("draw matches:",drawcount)
        elif count>usercount:
            print("...........................................")
            print("final ans computer win")
            print("user score",usercount)
            print("com score:",count)
            print("draw matches:",drawcount)
        else:
            print("...........................................")
            print("final ans you win")
            print("user score",usercount)
            print("com score:",count)
            print("draw matches:",drawcount)
            





    else:
        break