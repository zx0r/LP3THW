#Functional for mathematical operations

def add(a, b):
    print(f"ADDITION {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTION {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLICATION {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVISION {a} / {b}")
    return a / b

print("Let's do some calculations with functions!")

age = add(30, 5)
height = subtract(190, 4)
weight = multiply(35, 2)
iq = divide(250, 2)

print(f"Age: {age}, \nHeight: {height}, \nWeight: {weight}, \nIQ: {iq}")

#Puzzle as an optional chllenge, enter the code anyway

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("It turns out: ", what, "Can you calculate this manually!?")
