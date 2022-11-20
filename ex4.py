cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("In stock", cars, "cars")
print("M only", drivers, "drivers went to work")
print("It turns out that", cars_not_driven, "cars are empty")
print("We can transport today", carpool_capacity, "person")
print("Today you need to take", passengers, "person")
print("There wiil be approximately", average_passengers_per_car, "person in each car")
