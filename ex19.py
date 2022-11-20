def cheese_and_crackers(cheese_count, boxes_of_crackers):
     print(f"We have {cheese_count} cheeses!")
     print(f"We have {boxes_of_crackers} packs of chips!")
     print("Enough for a party!")
     print("Let's go!\n")

print("We can directly pass numbers to the function") 
cheese_and_crackers(20,30)

print("OR,we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even perform calculations within a function:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And combine variables with calculations:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


