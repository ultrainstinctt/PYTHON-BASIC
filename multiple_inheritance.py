class Pratap:
    def workout(self):
        print('i do workout everyday')

class Patu:
    def diet(self):
        print('i maintained my diet')


class Names(Pratap,Patu):
    pass
a = Names()
a.workout()
a.diet()