from nose.tools import *
from ex47.game import Room

def test_room():
    gold = Room("GoldRoom",
                """This room is full of gold to steal.
                There is a door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Testing the center room.")
    north = Room("North", "Testing the north room.")
    south = Room("South", "Testing the south room.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and fall into moo.")
    west = Room("Trees", 
                """There are trees here and you can head east.""")

    down = Room("Dungeon", "It's dark in here and you can go upstairs.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
