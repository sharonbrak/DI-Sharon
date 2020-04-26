#Exercise1 

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat('woopi',1)
cat2 = Cat('hop',10)
cat3 = Cat('hey',5)

def oldest(cats):
    oldestcat = cats[0]
    for x in cats:
        if x.age > oldestcat.age:
            oldestcat = x
    return oldestcat


my_cats=[cat1,cat2,cat3]
oldest_cat = oldest(my_cats)
print(oldest_cat.name)
print(f'The oldest cat is {oldest_cat.age} years old')

# Exercise 2

class Dogs():

    def __init__(self, nameDog,heightDog):
        self.nameDog = nameDog
        self.heightDog = heightDog
        self.winner = False
    
    def talk(self):
        print('Wouaf')
    
    def jump(self):
        newheight = 2*self.heightDog
        print(newheight)


davids_dog=Dogs('Rex',50)

print(davids_dog.nameDog)
print(davids_dog.heightDog)

sarahs_dog = Dogs('Sarah',20)
print(sarahs_dog.nameDog)
print(sarahs_dog.heightDog)

def bigger(dog1,dog2):
    if dog1.heightDog > dog2.heightDog:
        print(f'{dog1.nameDog} is the biggest')
        dog1.winner = True
    else:
        print(f'{dog2.nameDog} is the biggest')
        dog2.winner = True


bigger(davids_dog,sarahs_dog)
print(davids_dog.winner)
print(sarahs_dog.winner)


# Exercise 3 

class Zoo():

    def __init__(self,zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    
    def get_animals(self):
        print(" ".join(self.animals))

    def sell_animal(self,animalsold):
        print(f'Goodbye {animalsold}!')
        self.animals.remove(animalsold)

    def sort_animal(self):
        mydict = {}
        for x in self.animals:
            if x[0] in mydict:
                mydict[x[0]].append(x)
            else:
                mydict[x[0]] = []
                mydict[x[0]].append(x)

        self.mydict = mydict
    
    def getpen(self):
        print (self.mydict.items())
    

my_animals = ['bird', 'girafe', 'dog', 'cat', 'lion', 'bear']
myzoo = Zoo('Sharon Zoo')

print(myzoo.name)
print(myzoo.animals)

for x in my_animals:
    myzoo.add_animal(x)
myzoo.get_animals()
myzoo.sell_animal('cat')
myzoo.get_animals()
myzoo.sort_animal()
myzoo.getpen()
