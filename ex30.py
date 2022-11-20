people = 30
cars = 40
trucks = 15


if cars > people:
    print("Let's go by car.")
elif cars < people:
    print("We will not go by car.")
else:
    print("We can't choose.")

if trucks > cars:
    print("Too many buses.")
elif trucks < cars:
    print("Maybe take a bus!?")
else:
    print("We still can't choose.")

if people > trucks:
    print("Okay, let's take the bus.")
else:
    print("Fine, let's stay at home.")
