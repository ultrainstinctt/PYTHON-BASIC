s={10,20,50,60,52,8000}
print(s)


for a in s:
    print(a)




s1=set(s)
print("set=",s1)


s.remove(20)
print("remove=",s)


s.discard(10)
print("discard=",s)

print("pop=",s.pop())# randomly delete
print(s)

s.add(10000)
print("add=",s)

a=[10,20,30,50]
b={100,550,52,66,3,2522}
b.update(a)
print(b)