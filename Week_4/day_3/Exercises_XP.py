# Exercise 1 

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

mylist = []
for x in zip (keys,values):
    mylist.append(x)
print (mylist)

mydict = {}
for x in mylist:
    mydict[x[0]] = x[1]
print(mydict)


#Exercise 2 

store = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000, 
    'major_color': {
        'France':'blue', 
        'Spain': 'red',
        'US': ['pink', 'green']
    }
}

store['number_stores'] = 2


customers = store["type_of_clothes"]
print(f"Client of zara are: {', '.join([el for el in customers])}")


store['country_creation']='Spain'

if store['international_competitors'][0] != '':
    store['international_competitors'].append('Desigual')


del store['creation_date']

print(store['international_competitors'][-1])

print(f'The majors colors in the US are {store["major_color"]["US"][0]} and {store["major_color"]["US"][1]}')

len(store)

store.keys()

more_on_store = {
    "creation_date": 1975, 
    "number_stores": 10000 
}

store.update(more_on_store)
print(store['number_stores'])


#Bonus

store['stores_worldwide'] = {}

def addstore(country,number):
    if 'stores_worldwide' in store:
        store['stores_worldwide'][country]= number
print(store['stores_worldwide'])

store['add_store']= addstore

addstore('Israel',3)
print(store)
