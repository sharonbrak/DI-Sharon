#Daily Challenge 

birthdate = input('What is your birth date? (Enter it like this DD/MM/YYYY) ')
day = birthdate[0:2] 
month = birthdate[3:5]
year = birthdate[6:10] # or year = birthdate.split("/")[-1] 
curryear = 2020
age = int(curryear) - int(year)

numcandles = str(age)[-1]
print(numcandles)
x = "i"* int(numcandles)

toprint =   f'''
    ___{x}___
   |:H:a:p:p:y:|
 __|___________|__ 
|^^^^^^^^^^^^^^^^^|
|:B:i:r:t:h:d:a:y:|
|                 |
~~~~~~~~~~~~~~~~~~~
'''


if (int(year) % 4) == 0: 
    if (int(year) % 100) == 0: 
        if (int(year) % 400) == 0: 
            print(toprint)
            print(toprint)
        else: 
            print(toprint)
    else: 
        print(toprint)
        print(toprint)
else: 
    print(toprint)
