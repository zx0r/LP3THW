ten_things = 'Apples Oranges Crows Phones Light Sugar'

print("Wait, there are less then 10 objects.Let's fix this.")

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Bear', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print('We add: ', next_one)
    stuff.append(next_one)
    print(f"Now we have {len(stuff)} objects.")

print("So: ", stuff)
    
print("Let's do something with our objects.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))


