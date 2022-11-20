from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    
   def enter(self):
        print("This scene has not yet been set up.")
        print("Subclass and implement the enter() function.")
        exit(1)
        
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene('next_scene_name')

        current_scene.enter()

class Death(Scene):

    quips = [
             "You died.How sad it is.",
             "Your mother will be sad for you...you should have been smarter.",
             "You should have been such a jerk.",
             "Even my little puppy thinks better.",
             "When will you grow up, as your folder said."
    ]

    def enter(self):
        
        print(Death.quips[randint(0, len(self.quips)-1)])

class CentralCorridor(Scene):

    def enter(self):

        print(dedent("""
            Gothons from the planet Percale 25 have captured your
            ship and wiped out the entire team.You are the only one
            left aliveself.You need to steal the neutron bomb from
            the armory lab, lay here in the fuel bay and leav ship
            in an escape pod before it explodes.You run down the
            central corridor tothe weapons lab, when a gothon with
            red scaly appears in front of you with scin, rotten
            teeth and a clown suit.He hates looks at you and,
            blocking the way to the laboratory, pulls out a blaster
            to send you to the forefathers.         
        """))
        
        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                You quickly draw your blaster and start firing at
                get ready. His clown outfit spins on his body, interfering
                hit the target. All your shots have failed
                failed, and the blaster's charge ran out. Gothon costume that
                bought by his mother, hopelessly spoiled, so
                the alien in a rage draws a blaster and shoots
                in your head. In a panic, you try to escape and abruptly
                turning, you hit your head on the beam and lose
                consciousness. You died a heroic death.
            """))
            return 'death'



        elif action == "skip!":
            print(dedent("""
                Like a world class boxer you dodge and you slip past the
                Goton, out of the corner of your eye noticing that
                his blaster is pointed at your head. And here you
                slip and crash into the wall. From the blow you
                you lose consciousness. When you regain consciousness,
                you have time feel that the gothon is trampling on your head
                and devours you. The light fades before my eyes.
            """))
            return 'death'

        elif action == "joke":
            print(dedent("""
                Fortunately, you are familiar with the Goton culture and
                know that might make them laugh. You say bearded
                Neocolonies isomorphically relative to multiband hyperbolic 
                paraboloids, theoretically catarrhal. Gothon freezes,
                tries hold back laughter, and then begins to laugh 
                uncontrollably.While he's laughing, you take out your
                blaster and shoot I go to the head. He falls and you
                jump over him and run to the weapons laboratory.
            """))
            return 'laser_weapon_armory'

        else:
            print("DO NOT DO THIS!")
        return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You run into the weapons lab and start search the room
            to see if there are other Gotons hiding there.
            There is dead silence. You run to the far corner of the
            room and you find a neutron bomb in a protective container.
            On the front side of the container there is a panel with
            buttons and you need to enter the correct code to get the
            bomb. If you enter the wrong code 10 times,the container
            will be blocked and you won't be able to get the bomb.
            Please note that the code consists of 3 digits.
        """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print('WHACKKKK')
            guesses += 1
            guess = input('[keypad]> ')

        if guess == code:
            print(dedent("""
                The container opens with a click and releases blue gas.
                You pull out a neutron bomb and run into fuel 
                compartment to plant the bomb in the right place,
                activate it and have time to get off the ship.
            """))
            return 'the_bridge'

        else:
            print(dedent("""
                You hear the castle hum one last time and then
                you smell the burning - the castle has melted.
                You're staying in the gun shop until the gothons
                finally explode ship shot from your ship and you
                don't die.
            """))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You run into the fuel bay with the neutron bomb and
            you see five Gotons, unsuccessfully trying to control
            ship. One is uglier than the other, and everyone is
            in clown clothes suits, like the Gothon you killed.
            They don't get weapons, because they see a bomb in
            your hands and do not want to, so that you blow it up.
            The advantage is clearly on your side.
        """))

        action = input("> ")

        if action == "throw_bomb":
            print(dedent("""
                You activate the bomb in a panic and throw it into the crowd
                gotons, and then you jump to the airlock door. Straightaway
                after that, one of the gotons shoots you in the back.
                Dying, you see how other Gotons try in vain
                deactivate the bomb. You realize that the gothons too
                will perish. The light fades before my eyes.
            """))
            return 'death'

        elif action == "plant_bomb":
            print(dedent("""
                You point your blaster at the bomb in your hands.
                The Gotons raise their paws up and sweat in fear.
                You carefully, without turning away, approach the door and
                planting the bomb carefully, keeping the gotons on
                fly. You jump in the airlock and close the door
                with a blow on the button, and then with a blaster you melt
                a lock so that the Gotons cannot open it. Now
                you need to get into the escape pod and get away with
                ship to hell.
            """))         
            return 'escape_pod'

        else:
            print("IT IS NOT TO DO IT")
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You're rushing through the compartment with escape pods.
            Some of them can be damaged and explode during
            flight. There are five capsules in total, and you don't have time to
            inspect each for damage.
            Thinking for a second, you decide to sit in a capsule under number...
            Which capsule number do you choose?
        """))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                You jump into capsule number {guess} and press the button
                undocking. The capsule flies into space space, and then
                explodes with a bright flash, scattering pieces. You are dying.
            """))
            return 'death'
        
        else:
            print(dedent("""
                You jump into capsule number {guess} and press undock button.
                The capsule flies into space space and then sent to the planet
                nearby. You look out the window and see how your ship explodes.
                Its shards damage the fuel bay of the Gothon ship, and that one
                too shatters into pieces. Victory is yours!
            """))
            return 'finished'


class Finished(Scene):
    
    def enter(self):

        print("You wins! Great job.")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished' : Finished(),
    }
    
    def __init__ (self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
