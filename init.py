class Abc:
    def __init__(self):
        print("fdsjfffbh")

    def swim(self):
        print("i am swiming")


fliper = Abc()
fliper.swim()

####################################################

class Enemy:

    def __init__(self, x):
        self.energy =x
    
    def get_energy(self):
        print(self.energy)


pb = Enemy(5)
sd = Enemy(20)
pb.get_energy()
sd.get_energy()