import random
random_no=random.randrange(1,101)
user=int(input("enter a no between 1 to 100 :"))


if user>random_no:
        print("high")
      
        print(random_no)
elif user<random_no:
        print("low")
        
elif user==random_no:
        print("equal")
    
else:
        print("invalid no")
