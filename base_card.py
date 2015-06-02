__author__ = 'ian'
class BaseCard:
    name = ""
    attack = 0
    defense = 0
    critical = 0
    grade_of_card = 0
    clan_of_card = " "
    type_of_card = " "
    abilities_of_card = " "
    image_of_card = " "
    serial_num_of_card = 0

    def __init__(self, a, b, c, d, e, f, g, h, i):
        self.attack = a
        self.defense = b
        self.critical = c
        self.grade_of_card = d
        self.clan_of_card = e
        self.type_of_card = f
        self.abilities_of_card = g
        self.image_of_card = h
        self.serial_num_of_card = i


