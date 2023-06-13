list=[10,20,30,40,50]
print(list)

#count
count=list.count(10)#how many time that element in list
print("count=",count)
#max
m=max(list)
print("max",m)


#sort
list.sort()
print("sort=",list)

#reverse
list.reverse()
print("reverse",list)

#index
l=["hello","pratap"]
a=l.index("hello")
print("index=",a)

#min
min=min(list)
print("min",min)

#update list
list[0]=60
print("update",list)


del(list[2])# delete
print("delete",list)

#pop
list.pop(3)
print("pop",list)

#remove
list.remove(40)
print("remove",list)

#insert
list.insert(0,100)
print("insert",list)

#append
list.append(150)
print("append",list)

#extend
l=[7000,56000]
list.extend(l)
print("extend",list)



#clear
list.clear()
print("clear",list)

