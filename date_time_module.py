import datetime

x = datetime.datetime.now()     #return current date and time
print(x)

y=datetime.datetime(2021,1,18)
print(y) 

now=datetime.datetime.now()
year=now.strftime("%Y")
month=now.strftime("%b")

print("year",year)
print("month",month)