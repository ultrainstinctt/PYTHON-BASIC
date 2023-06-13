l=[10,20,30,52,63,100]
l1=[54,63,85,99,63,3]
for a,b in zip(l,l1):# same time iterrate by zip but  same size list
    print(a,b)

#2nd logic
t=len(l)
for i in range(t):
    print(l[i],l1[i])