i = 0
numbers = []

while i < 6:
    print(f'At the beginning, the value of i is {i}')
    numbers.append(i)

    i = i + 1
    print('Current values: ', numbers)
    print(f'At the end the value of i is {i}')

print('Values: ')

for num in numbers:
    print(num)
    
