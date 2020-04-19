# #Exercise 1

cars = 100
drivers = 30
passengers = 90 
groupsof4 = int((passengers - (passengers%4))/4)
busycars = groupsof4 + 1
emptycars = cars - busycars
maxpassengers = drivers*4
averagepassenger = passengers / busycars

report = f'Daily Report\n\nCars available: {cars}\nDrivers registered: {drivers}\nEmpty cars today: {emptycars}\nPassengers that can be transported today: {maxpassengers}\nAverage passengers per car: {averagepassenger}'
print(report)


# Exercise 2

choice = input('Please enter a letter: ')

if choice == 'a' or choice == 'e' or choice == 'i' or choice == 'o' or choice == 'u' or choice == 'A' or choice == 'E' or choice == 'I' or choice == 'O' or choice == 'U':
    print('This is a vowel')
else:
    print('This is a consonant')


# Exercise 3 - In progress

# Exercise 4 

mytext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
len(mytext)

# Exercise 5 - In progress

# Exercise 6 - In progress
