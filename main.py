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
        cls.choice = ""
        try:
            cls.choice = int(input('Input:'))
        except ValueError:
            print("Not a number")
        if cls.choice == 1:
            print("Starting option 1")
            cards = []
            for file in os.listdir("Card_Json_Data/"):
                c = Card.from_file("Card_Json_Data/" + file)
                cards.append(c)
            print(len(cards))
            print("Would you like to see the card database?")
            sinput = str(input('Input:'))
            if sinput == "yes":
                for i, element in enumerate(cards):
                    print(str(cards[i].name) + str("\n") + str(cards[i].power) + str("\n") + str(cards[i].shield)
                          + str("\n") + str(cards[i].critical) + str("\n") + str(cards[i].grade) + str("\n")
                          + str(cards[i].clan))
            elif sinput == "no":
                print("moving on")
            else:
                print("Error")

        elif cls.choice == 2:
            print("Starting option 2")
        elif cls.choice == 3:
            print("Starting option 3")
        elif cls.choice == 4:
            print("Starting option 4")
        else:
            print("Invalid Response")
Runtime.main()
