class Boy:


    gender =  "male"        # any time use class variable


    def __init__(self, name):
        self.name = name


r = Boy('Pratap') #instans variable is for specific object
s= Boy('shayam')

print(r.gender)
print(s.gender)
print(r.name)
print(s.name)