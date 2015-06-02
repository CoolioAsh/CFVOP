__author__ = 'ian'
from Card import *
import os
class Runtime:
    @classmethod
    def main(cls):
        print("Starting Cardfight Vanguard!! Online Python Version")
        print("Following options are allowed")
        print("1. Creation of Cards and Browsing of Cards")
        print("2. Creation of Decks and Browsing of Decks")
        print("3. Starting a Game and Browsing Old Games")
        print("4. Options and Settings")
        try:
            choice = int(input('Input:'))
        except ValueError:
            print("Not a number")
        if choice == 1:
            print("Starting option 1")
            cards = []
            for file in os.listdir("~/Documents/JavaProjects/Cardfight Vanguard Online/src/alpha/CardRawData/"):
                c = Card.from_file(file)
                cards.append(c)
        elif choice == 2:
            print("Starting option 2")
        elif choice == 3:
            print("Starting option 3")
        elif choice == 4:
            print("Starting option 4")
        else:
            print("Invalid Response")
Runtime.main()
