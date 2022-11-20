
#list
heirs = ['brown', 'blonde', 'redhead']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'peach', 'apricot']
change = [1, 'chervonets', 2, 'fifty dollars', 3, 'hundred']

#the for loop of the first type processes the list
for number in the_count:
    print(f'Counter: {number}')

#same is above
for fruits in fruits:
    print(f'Fruit: {fruits}')

#can elso handle nixed lists
#note that {} characters are used,as unknown
#value type
for i in change:
    print(f'I got {i}')

#also we can create lists, start with empty
elements = []

#then use the range() function to limit the range
for i in range(0, 6):
    print(f'Adding {i} to the list')
    #append - function for adding elements the list
    elements.append(i)

#now we display them
for i in elements:
    print(f'Element number: {i}')
    
