s="hi tanu can we go for a date"
print(s[6])
print(s[-1])
print(s[0:7])
print(s[0:])
print(s[0::2])#increment of 2 slicing
print(s[-1::-1])#reverse string
print(s[-1::-2])


n="hi pussy cat!"
t=len(n)
for i in  range(t-1,-1,-1):
    print(n[i])

#lower case string
low="HI PRTIMA HOW are you?"
n=low.lower()
print(n)

#upper case string
upp="you aRe mY Enemy"
m=upp.upper()
print(m)

#title case
t="you aRe mY Enemy"
m=t.title()
print('tite case:',m)


#captalize
upp="you aRe mY Enemy"
m=upp.capitalize()
print(m)

#find
f="pratap loves nobody"
print(f.find('l'))
print(f.find('p'))
print(f.find('p',2))
print(f.index('a'))#index

f="pratap"
print(f.isalpha())
print(f.isdigit())
print(f.isalnum())

#chr & ord func
a=65
print(chr(a))
a='A'
print(ord(a))

#string format
a= "hi {} welcome to vscode{}".format("pratap",2.0)
print(a)

a= "hi {1} welcome to vscode{0}".format("pratap",2.0) #hi 2.0 welcome to vscodepratap  is the  output
print(a)