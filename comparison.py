__author__ = 'ian'
class Comp:
    @classmethod
    def base_comp(cls, a, b):
        if a > b:
            print("Greater")
            return 1
        elif a < b:
            print("Lesser")
            return -1
        elif a == b:
            print("Equal in Value")
            return 0
        else:
            print("Error")
            return None
