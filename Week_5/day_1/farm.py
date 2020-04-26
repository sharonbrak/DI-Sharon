class Farm():

    def __init__(self, name):
        self.name = name
        self.list = {}

    def add_animal(self, animal, number=1):
        if animal in self.list.keys():
            self.list[animal] += number 
        else: 
            self.list[animal] = number 
           

    def get_info(self):
        print(f'{self.name}\'s farm')
        for animal in self.list:
            quantity_to_print = self.list[animal]
            name_to_print = animal 
            if self.list[animal] > 1:
                name_to_print += 's'
            print(f'{name_to_print}: {quantity_to_print}')


    def get_animal_types(self):
        return self.list.keys()

    def get_short_info(self):
        types_of_animals = list(self.get_animal_types())
        sentence = ", ".join(a.lower() for a in types_of_animals)
        print(f'{self.name}\'s farm has ' + sentence)
