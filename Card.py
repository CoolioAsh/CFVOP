__author__ = 'ian'
import json
import os.path
class Card:
    def __init__(self, name, power, shield, critical, grade, clan):
        self.name = name
        self.power = power
        self.shield = shield
        self.critical = critical
        self.grade = grade
        self.clan = clan

    @classmethod
    def from_file(cls, filename):
        card_json = os.path(filename).text()
        card = Card(card_json["name"], card_json["power"], card_json["shield"], card_json["critical"],
                    card_json["grade"], card_json["clan"])
