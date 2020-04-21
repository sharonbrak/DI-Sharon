# Get a string from the user. The user must provide a string that is 10 characters long.
# Inform the user what the first and last characters of the string are
# ‘Build’ the string up: print the first character, then the first 2, then the first 3, etc., 
# until you print
# the entire string.
# Swap some of the characters around, then print out this jumbled-up string to the user. Be sure to label it appropriately.

choice = input('Give a string that is 10 char long: ')

firstchar = choice[0]
lastchar = choice[9]
print(f'Your first char is {firstchar}\nYour last char is {lastchar}')

stri =''
for x in choice:
    stri = stri + x
    print(stri)

newchoice = print(choice[9] + choice[8] + choice[1] + choice[2] + choice[3] + choice[4] + choice[5] + choice[6] +choice[7])   