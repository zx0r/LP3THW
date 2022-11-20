from sys import exit

def gold_room():
    print("It's full of gold.How many kg will you carry?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much  = int(choice)
    else:
        dead("Fi, you need to enter a number.")

    if how_much < 50:
        print("Gorgeus! You are not greedy, so yoy win!")
        exit(0)
    else:
        dead("Oh you greedy!")

def bear_room():
    print("Bear sleeps here")
    print("The bear has a barrel of honey.")
    print("The bear closed the exit door.")
    print("How to move the bear?Take away honey or tease a bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "Take away the honey":
            dead("The bear looked at you and hit you in the face with its paw.")
        elif choice == "Tease the bear" and not bear_moved:
            print("The bear moved away from the door.")
            print("You can enter it.Tease a bear or enter the door?")
            bear_moved = True
        elif choice == "Tease a bear" and bear_moved:
            print("The bear got angry and bit off your leg.")
        elif choice == "Enter the door" and bear_moved:
            gold_room()
        else:
            print("Enter one of the suggested actions.")

def cthulhu_room():
    print("The great and terrible Cthulhu is watching you.")
    print("He looks at you and you start going crazy.")
    print("Run or fight!?")

    choice = input("> ")

    if "run" in choice:
        start()

    elif "start fighting" in choice:
        dead("Hm, maybe even win!")
    
    else:
        cthulhu_room()

def dead(why):
    print("why, Great!")
    exit(0)

def start():    
    print("You are in dark room.")
    print("There are two doors leading from here, left and right.")
    print("Where will you turn!?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You go from room to room until you are hungry.")

start()




