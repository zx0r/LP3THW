print("""
      You are in dark room with two doors.
      Which door wiil you enter - 1 or 2!?   
      """)

door = input("> ")

if door == "1":
    print("In this room, a giant bear is eating 'Frienship' cheese.")
    print("Your actions!?")
    print("1. I'll take the cheese.")
    print("2. I'll yell in the bears ear.")

    bears = input("> ")

    if bears== "1":
        print("The bear grabbed your face.That's great!")
    
    elif bears == "2":
        print("The bear bit your leg.That's great!")

    else:
        print(f"Great, this action {bears} was the only correct one.")
        print("The bear run away.")

elif door == "2":
    print("You are looking inti the endless abyss of Cthulhu's eyes.What are you doing!?")
    print("1. I'll tell Cthulhu about swamps in Siberia.")
    print("2. I'll pat the yellow buttons on my jacket.")
    print("3. I'll try to whistle the song 'Black Raven'.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("You survived because Cthulhu turned to jelly.")
        print("Just great!")

    else:
        print("Madness seized you and you fell into the pool of rot.")
        print("Just great!")

else:
    print("Madness seized you and you tore your face to pieces.Great job!")
