#mystuff = {'apple': "I'm - APPLE"}

#class MyStuff(object):

#    def __init__(self):
#        self.tangerine = "Let run clumsily"

#    def apple(self):
#        print("I'm - THE SWEETEST APPLE!")

#thing = MyStuff()
#thing.apple()
#print(thing.tangerine)


#Dictionary method
#mustuff['apples']

#Method with module
#mystuff.apples()
#print(mystuff.tangerine)

#Method with class
#thing = MyStuff()
#thing.apples()
#print(thing.tangerine)

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Can I have your birthday",
                   "Expensive gifts to give,",
                   "But these spring nights"])            

bulls_on_parade = Song(["Far, far away, who is grazing in the medow?",
                        "Drink, children, milk, you will be healthy!"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
