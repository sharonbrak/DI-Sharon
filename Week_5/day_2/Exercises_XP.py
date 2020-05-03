# Exercise 1 

from typing import List, Dict, Union, Optional

class Family():
    def __init__(
            self, last_name: str, members: List[Dict]):
        self.name = last_name 
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f'Congratulations to the new born, {kwargs["name"]}!')

    def is_18(self, name_check: str) -> Optional[bool]:
        for member in self.members:
            if member['name'] == name_check:
                if member['age'] > 18:
                    return True
                else:
                    return False
        print('This member does not exist in the family')
        return None
        

    def __repr__(self) -> str:
        sentence_1 = f'The family is named {self.name}.\nAnd here are its members:\n'
        sentence_1 += '\n'.join([f"- {member['name']} is {member['age']} years old. It is a {member['gender']}." for member in self.members])
        return sentence_1


# 1-
scherman_family = Family(
    last_name='Scherman',
    members=[{'name': 'Mathias', 'age': 29, 'gender': 'Male', 'is_child': True}])

scherman_family.born(name='Martin', age=0, gender='Male', is_child=True)

# kwargs = {'newname': 'Martin', 'age': 0, 'gender': 'Male', 'is_child': True}

# 2-

print(scherman_family.is_18('Mathias'))
print(scherman_family.is_18('Martin'))
print(scherman_family)


# Exercise 2

class TheIncredibles(Family):
    
    def use_power(self):
        for member in self.members:
            if member['age'] > 18:
                print(f"{member['name']}, You have a great power: {member['power']}")
            else:
                print(f"{member['name']}, You have no power here!")

    def incredible_presentation(self) -> str:
        sentence_1 = f'The family is named {self.name}.\nAnd here are its members:\n'
        sentence_1 += '\n'.join([f"- {member['name']} is {member['age']} years old. It is a {member['gender']}. She has a superpower: {member['power']}. And her nickname is {member['incredible name']}." for member in self.members])
        return sentence_1


my_incredible_family = TheIncredibles(
    last_name = 'Brakha',
    members = [{'name': 'Sharon', 'age': 30, 'gender': 'Female', 'is_child': True, 'power':'Can read minds', 'incredible name':'Pti Chat'}, 
    {'name': 'Ele', 'age': 16, 'gender': 'Female', 'is_child': True, 'power':'can smile all the time', 'incredible name':'Loulou'}]
    )

my_incredible_family.use_power()

print(my_incredible_family.incredible_presentation())
print(my_incredible_family)

my_incredible_family.born(name='Jack', age=0, gender='Male', is_child=True, power= 'Unknown Power')