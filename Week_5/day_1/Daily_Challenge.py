#1

import itertools

class UniqueSubsets():

    def __init__(self,listnums):
        self.listnums = listnums

    def findsubsets(self, n): 
        return list(itertools.combinations(self.listnums, n))


my_nums = UniqueSubsets([4, 5, 6])

my_list = []
for x in range (4):
    my_list = my_list + my_nums.findsubsets(x)
print(my_list)


#2

class SubsetsSum0():

    def __init__(self,listnums):
        self.listnums = listnums

    def findsubsets_sum0(self): 
        return [a for a in itertools.combinations(self.listnums, 3) if sum(a) == 0]


my_list2 = SubsetsSum0([-25, -10, -7, -3, 2, 4, 8, 10])
print(my_list2.findsubsets_sum0())