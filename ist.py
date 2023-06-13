print("hello")
#FOR LOOP 

for f in range(5,15):
    print(f)

#WHILE LOOP

pratap=50
while pratap < 60:
   print (pratap)
   pratap += 1

# CONTINUE USE

numbertake=[52,63,89,66,55]
print("here are the number are still avaliabel")
for n in range(45,52):
    if n in  numbertake:
        continue
    print(n)


def pratap():  #functions
    print("hey! hello world ")

pratap()
pratap()
pratap()



def bitcoin(btc):
    amount = btc*100
    print(amount)

bitcoin(5)
bitcoin(5.56)
bitcoin(100)

def allowed_dating_age(my_age):
    girlsAge = my_age/2 +7
    return girlsAge

allowed_dating_age(24)
limit = allowed_dating_age(23)# it cant show the output because its equal to return value  ( by Pratap)
print("pratap can date a girl" ,limit,"or older")

'''
#default values and argument

def get_gender(sex ='unknown'):
    if sex is 'm':
        sex ="male"
    elif sex is 'f':
        sex = "female"
    print(sex)

get_gender('m')
get_gender('f')
get_gender()
'''

#veriable scope
a=789456

def corn():
    b=456
    print(b)
    print(a)

def fuzzy():
    print(a)
   # print(b) here var b cant execute whenever a var create in a function only  these function access that variable. (by pratap)

corn()
fuzzy()


#keyword_argument
def dumb_sentence(name='Pratap',action ='ate',item ='chicken'):
    print(name,action,item)
dumb_sentence()
dumb_sentence("ram","farts","gently")
dumb_sentence(item='awesome')
dumb_sentence(item='awesome',action='is')


def add_number(*args):# here use *  for bunch of argument
    total = 0
    for a in args:
        total += a
        print(total)
add_number(3)    
add_number(3,35)
add_number(5,88,55,66,78,333)

# Unpacking argument
def health_calculator(age,apple_ate,cigs_smoked):
    answer = (100-age) +(apple_ate*3.5)-(cigs_smoked*2)
    print(answer)

data= [27,28,0]
health_calculator(data[0],data[1],data[2])

#sets
grocerices = {'apple','milk','biscuit','beer','oldmonk','gold flake','black dog'}
print(grocerices)

if 'milk' in grocerices:
    print("you already have milk ")
else:
    print("you havenot milk bro")

#dictionary

classmates ={'tony': ' cool but smells', 'pratap' :' sits behind me','rum': ' ask many question'}
print(classmates)
print(classmates['pratap'])
print(classmates['rum'])

for k, v in classmates.items():
    print(k + v)


#binary oparators

a= 10
b= 8

print(bin(a))
print(bin(b))
print( bin(a&b), a&b) #AND
print(bin(a|b),a|b)#OR
print(bin(a^b),a^b)#XOR
print(bin(~(a^b)) ,~(a^b))#XNOR

#TABLE
for i in range(1,11):
    print(2,'X' ,i, '=',2*i)
#PRINT TABLE USING  FUNCTION

def table(num):

    for i in  range(1,11):
        print(n,'X' ,i, '=',num*i)
n=int(input("Please enter a number : "))

table(n)