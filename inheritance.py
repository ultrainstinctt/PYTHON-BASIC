class parent():

    def print_last_name(self):
        print('Bhattacharya')



class Child(parent):

    def print_first_name(self):
        print('Pratap')
''' def print_last_name(self):
        print('Bhattacharjee')'''


a = Child()
a.print_first_name()
a.print_last_name()