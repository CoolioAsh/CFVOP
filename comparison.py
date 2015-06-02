__author__ = 'ian'
class Comp:
    @classmethod
    def basecomp(cls, a, b):
        if a > b:
            print("Yep")
            return 1
        elif a < b:
            print("Nope")
            return -1
        elif a == b:
            print("Equals")
            return 0
        else:
            print("Error")
            return None
