# Exercise 1

fruits = input('What is/are your favorite fruits?  ')
print(fruits)
type(fruits)

mylist = fruits.split(' ')

newfruit = input('Type another fruit: ')
if newfruit in mylist:        
    print('you chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy it too!')

if len(mylist) >=2:
    last = mylist[-1]
    mylist.append("and")
    mylist.append(last)


Exercise 2

mypassword =input('Give me a password: ')

# We check if it includes a digit

ifdigit = []
for x in mypassword:
    if x.isdigit():
        print('yes')
        ifdigit.append(x)
    else:
        print('no')
print(ifdigit)

#Another way to check if digit 
# any([char.isdigit() for char in password])



if mypassword.upper() != mypassword and mypassword.lower() != mypassword and len(ifdigit)>0 and '@' in mypassword or '#' in mypassword or '$' in mypassword and len(mypassword)>=6 and len(mypassword) <=12:
    print('Great!')
else: 
    print('OOOPS!')




# Exercise 3 

for x in range(3,31):
    if x%3 == 0: 
        print(x)


# Exercise 4 

mylist = [1,2,3,4,5,6,7,8,9,10]
insertindex = 4
item = 'here'

''' We want to insert in index 5 the word 'here' '''

mylist1 = mylist[0:int(insertindex)]
mylist2 = mylist[int(insertindex):len(mylist)]
mylist1.append(item)
newlist = mylist1 + mylist2
print(newlist)


# Exercise 5 

# Exercise 6

Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700.

for x in range(1500,2701):
    if x % 7 == 0 and x % 5 ==0:
        print(x)


# Exercice 7 

mystring = 'hdzio hzias hzau hzuszajjo'

numspace = 0
for x in mystring:
    if x == " ":
        numspace +=1
print(numspace)


# Exercice 8

mystring = 'hdzio hzias hzau hzuszajjo'
len(mystring.split())
