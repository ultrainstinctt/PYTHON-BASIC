course={
    'c++':{'duration':'1 month','fees':100000},
    'python':{'duration':'2 month','fees':600000},
    'java':{'duration':'3 month','fees':50000}
    
    }
print(course)
print(course['java'] ['fees'])

for a,b in course.items():
    print(a,b['duration'],b['fees'])