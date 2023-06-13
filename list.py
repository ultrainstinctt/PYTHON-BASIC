list =[10,20,30,40,50,"hello"]
print(list)
print(list[3],list[5])
print(list[0:2])
print(list[0::2])
print(list[3:])
print(list[-1::-2])
print(list[-1::-1])

t=len(list)
for i in range(t-1,-1,-1):

    print(list[i],"    address in   ",i)

#add list
l1=[10,20,30,40,60,11,52,63]
l2=[55,66,22,33,55,44,70,45]

l1.sort()
l2.sort()

l3=l1+l2
print(l3)

l1.append(l2)
print(l1)


#zip list
l1=[10,20,30,40,60,11,52,63]
l2=[55,66,22,33,55,44,70,45]

for a,b in zip(l1,l2):
    print("zipping",a,b)


