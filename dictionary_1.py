d={
    'course' : 'python',
    'fees' :80000,
    'duration':'2month'
}
c=d.get('course')
print(c)
c1=d['course']
print(c1)

for a,b in d.items():
    print(a,b)
    
del d['fees']
print(d)

d.update({'course':'c++'})
print(d)

d['desc']="this is that"
print(d)