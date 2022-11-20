#Link diafram of abbreviations with country names
states = {
    'Russia':'RU',
    'Germany':'DE',
    'Uzbekistan':'UZ',
    'Zimbabwe':'ZW',
    'Turkey':'TR'
}

#Creation of a basic of countries and some cities in them
cities = {
    'UZ':'Gazli',
    'TR':'Sarygerme',
    'DE':'Munich'
}

#adding multiple cities
cities['ZW'] = 'Gveru'
cities['RU'] = 'Moscow'

#withdrawal of some cities
print('-' * 10)

print('In the country ZW there is a city: ', cities['ZW'])
print('In the country RU there is a city ', cities['RU'])

#Withdrawal of some countries
print('-' * 10)

print('Abbreviation Turkey: ', states['Turkey'])
print('Abbreviation Germany:', states['Germany'])

#Performed taking into account the country and the dictionary of cities
print('-' * 10)

print('There is a city in Turkey: ', cities[states['Turkey']])
print('There is a city in Germany: ', cities[states['Germany']])

#Display of abbreviations of all countries
print('-' * 10)

for state, abbrev in list(states.items()):
    print(f"{state} has an Abbreviation {abbrev}")

#Output of all cities in countries
print('-' * 10)

for abbrev, city in list(cities.items()):
    print(f"In the country {abbrev} there is a city {city}")


#And now both data types at once
print('-' * 10)

for state, abbrev in list(states.items()):
    print(f"In the country {state} abbreviation used {abbrev}")
    print(f"And there is a city {cities[abbrev]}")

print('-' * 10)

#safely getting the abbreviation of a country that is not represented
state = states.get('USA')

if not state:
    print("I'm sorry, the USA does not exist or has been destroyed.")

#Getting city with default value
city = cities.get('US', 'does not exist')
print(f"In the country 'US' there is a city: {city}")


    
