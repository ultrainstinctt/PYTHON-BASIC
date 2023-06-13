t=(10,20,62,40,10,20)
print(type(t))

n=t[3]
print(n)

l=len(t)
for a in range (l):
   # print(a)
    print(t[a])

min=min(t)
print("min=", min)


max=max(t)
print("max=", max)


count =t.count(10)
print("count=",count)

index=t.index(40)
print("index=",index)


sum=sum(t,10)
print('sum=',sum)