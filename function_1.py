def patu():                     #function defination 
    print("hi i am your bf")

patu()                           #callin the function

#FUNC WITH ARGUMENT
def sum(a,b):
    c=a+b
    print("sum=",c)
a=int(input("enter a no:"))
b=int(input("enter 2nd no:"))
sum(a,b)



def sum2(a,b=10):
    c=a+b
    print("sum2=",c)

a=int(input("enter a no:"))  
sum2(a) 




def sum3(a,b=10):
    c=a+b
    return c
a=int(input("enter a no: "))
x= sum3(a)
print("the sum =",x)