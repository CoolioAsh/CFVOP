__author__ = 'ian'
import json
class Card:
    def __init__(self, name, power, shield, critical, grade, clan):
        self.name = name
        self.power = power
        self.shield = shield
        self.critical = critical
        self.grade = grade
        self.clan = clan
        self.state_of_card = True
        self.state_of_lock = False
        self.state_of_tap = False

    @classmethod
    def from_file(cls, filename):
        json_file = open(filename, "r")
        json_string = json_file.read()
        json_file.close()
        card_json = json.loads(json_string)
        card = Card(**card_json)
        return card
