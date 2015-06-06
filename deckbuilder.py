__author__ = 'ian'
from Card import *
class DeckBuilder:
    def __init__(self, b):
        a = 50
        deck = []
        for s in range(0, len(b)):
            print("You are on card " + b[s].name + ", do you wish to add it to the current deck?")
            if str(input("Input:")) == "yes":
                deck.append(Card.from_file(b[s]))
                a - 1
                print("You now have " + a + " number of card positions left")
            else:
                print("Moving on")

    #def test_deck(self):
        #print("test")
