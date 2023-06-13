l=[]
for a in range (1,101):
    #print(a)
    l.append(a)
print(l)

#List comprehension 
#we can do conditional things
n=[m for m in range(1,101)  ]
print(n)

#we can do conditional things
n=[m for m in range(1,101) if m%2==0 ]
print(n)

s="pratap"
a=[g for g in s]
print(a)