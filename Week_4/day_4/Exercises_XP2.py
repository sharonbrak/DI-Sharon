#Exercise 1 

CURRENT_YEAR = 2020
CURRENT_MONTH = 4
CURRENT_DAY = 25

def get_age(year, month, day):
    if month > CURRENT_MONTH:
        return CURRENT_YEAR - year - 1 
    elif month < CURRENT_MONTH:
        return CURRENT_YEAR - year
    elif month == CURRENT_MONTH:
        if day > CURRENT_DAY:
            return CURRENT_YEAR - year - 1
        elif day <= CURRENT_DAY:
            return CURRENT_YEAR - year

print(get_age(1983,4,25))

AGE_F = 62
AGE_M = 67


def can_retire(gender, date_of_birth):
    year = int(date_of_birth.split('/')[0])
    month = int(date_of_birth.split('/')[1])
    day = int(date_of_birth.split('/')[2])
    if gender == 'M':
        if int(get_age(year,month,day)) >= AGE_M:
            print('Man,You can retire')
            return True
        else:
            print('sorry guy, your can\'t retire yet')
            return False
    elif gender == 'F':
        if int(get_age(year,month,day)) >= AGE_F:
            print('Girl,You can retire')
            return True
        else:
            print('sorry girl, your can\'t retire yet')
            return False


print(can_retire('M', '1955/9/27'))
    
