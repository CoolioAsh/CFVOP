__author__ = 'ian'
from Card import *
class DeckBuilder:
    def __init__(self, a, b):
        deck = []
        for s in range(0, (a - 1)):
            deck.append(Card.from_file(b[s]))

    def test_deck(self):
        print("test")
