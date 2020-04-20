# Exercise  

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)

basket.remove("Banana")
print(basket)

basket.remove("Blueberries")
print(basket)

basket.append("Kiwi")
print(basket)

newlist = ['Apples']
basket = newlist + basket
print(basket)

count = basket.count('Apples')
print(count)

basket = []
print(basket)

# Exercise1  

myset = {2,7,9}
myset.add('5')
myset.add('3')
print(myset)

myset.remove('3')
print(myset)

friend_fav_numbers= {10,20,30}
newset = myset.union(friend_fav_numbers)
print(newset)

# Exercise2

mytuple = (1,2,3,4,5)
#Cant't add items to a tuple
#Can't remove items from a tuple
newtuple = (10,20,30,40)
fulltuple = mytuple + newtuple
print(fulltuple)
print(type(fulltuple))


# Exercise 3

    #Option1 

mylist = []
for x in range(3, 11):
    mylist.append(x/2)
print(mylist)


    #Option2

mylist = []
x = 1.5
while x <= 5:  
    mylist.append(x)
    x+= 0.5
print(mylist)

# Exercice 4

topp = input('Give me a new pizza topping: ')

while topp != 'quit':
    print(f'I will add {topp} to your pizza!')
    topp = input('Give me a new pizza topping: ')

# Exercice 5

while True:
    age = input('What is your age?')
    if int(age)<3:
        print('Your ticket is free')
    elif int(age)>=3 and int(age)<=12:
        print('Your ticket is 10 dolar')
    elif int(age)>12:
        print('Your ticket is 15 dolar')


# Exercice 6

mylist = [1,2,3,4,5,'string',7,8,9]
x=0
while x <= len(mylist) :
    print(mylist[(len(mylist)-1)-x]) 
    x += 1

# Exercice 7

#Solution 1 - With pre-set Dictionnary

family = {
    "Father":60, 
    "Mother":50, 
    "Daughter":17, 
    "Son":11, 
    "Baby":1
    }

print(family.items())

total = 0
for name , age in family.items():
    if age <=3:
        continue
    elif age < 12:
        total += 10
    else:
        total += 15

print(total)

#Solution 2 - With pre-set Dictionnary


family = ["Father","Mother","Daughter","Son","Baby"]
total = 0
for x in family:
    age = input(f'Hey {x}, how old are you dear? ')
    if int(age) <= 3:
        continue
    elif int(age) < 12:
        total += 10
    else:
        total += 15

print(total)


#Exercise 8

mylist = [1,2,3,4,5,'string',7,8,9]

x=0
while x <= len(mylist)  :
    print(mylist[x])
    x +=2

# Exercise 9

group = ["John","Marc","Sophie","Jenny","Bob"]
allowedpeople =[]

for x in group:
    age = input(f'Hey {x}, how old are you? ')
    if int(age) >= 16 and int(age) <= 21:
        print('You are allowed to enter! I just added you to the list')
        allowedpeople.append(x)
    else:
        print('Sorry dear, GO HOME!')

print(allowedpeople)

# Exercise 10


group = ["John","Marc","Sophie","Jenny","Bob"]

for x in group:
    age = input(f'Hey {x}, how old are you? ')
    if int(age) < 16:
        group.remove(x)

print(group)