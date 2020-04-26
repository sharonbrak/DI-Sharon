# Exercise 1: Restaurant Menu Manager

class MenuManager():

    def __init__(self, menu):
        self.menu = menu 

    def add_item(self,name, price, spice, gluten):
        new_item=[name,price,spice,gluten]
        name_item='item ' + name
        self.menu[name_item] = new_item


    def update_item(self,name, price, spice, gluten):
        item_to_check = [name,price,spice,gluten]
        for x in self.menu:
            if item_to_check[0] == self.menu[x][0]:
                self.menu[x] = item_to_check
                return
        print('Its not there!!!')


    def remove_item(self,name):
        for x in self.menu:
            if name == self.menu[x][0]:
                del self.menu[x]
                return
        print('Its not there!!!')


shar_rest =  MenuManager({
    'item1' : ['Soup',10,'B',False],
    'item2' : ['Hamburger',15,'A',True],
    'item3' : ['Salad',18,'A',False],
    'item4' : ['French Fries',5,'C', False],
    'item5' : ['Beef Bourgignon',25,'B',True]
})

shar_rest.add_item('couscous',40,'C',True)
print(shar_rest.menu)

shar_rest.update_item('couscous', 25,'B',False)
print(shar_rest.menu)

shar_rest.update_item('pasta', 25,'B',False)
print(shar_rest.menu)

shar_rest.remove_item('couscous')
print(shar_rest.menu)

shar_rest.remove_item('rice')


# Exercice 2 : Old MacDonald’s Farm

from farm import Farm

mcdonald = Farm('McDonald')
quick = Farm('Quick')

mcdonald.add_animal('Cow',5)
mcdonald.add_animal('Sheep')
mcdonald.add_animal('Sheep')
mcdonald.add_animal('Goat',12)
mcdonald.add_animal('Giraffe',1)


mcdonald.get_info()


# Exercice 3 : Old MacDonald’s Farm

# 1 - Already done 

# 2 

print(sorted(list(mcdonald.get_animal_types())))

mcdonald.get_short_info()