
#Exercise 1 

import math  

class Circus():

    def __init__(self,radius=1):
        self.radius = radius 

    def perimeter(self):
        return 2 * math.pi * self.radius 

    def area(self):
        return math.pi * pow(self.radius,2)


#Exercise 2

import random 

class Mylist():

    def __init__(self, my_list):
        # Check that my_list is indeed a list
        if type(my_list) is not list:
            print('error')
            return
        self.mylist = my_list

    def reverse(self):
        return self.mylist[::-1]
    
    def sortedlist(self):
        return sorted(self.mylist)

    def random(self):
        return random.sample(range(100),len(self.mylist))


sharonlist = Mylist([2, 5, 8, 1, 23, 10])
print(sharonlist.reverse())
print(sharonlist.sortedlist())
print(sharonlist.random())


