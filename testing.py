__author__ = 'ian'
class MyClass(object):
    i = 123

    def __init__(self, my_i=345):
        self.i = my_i

a = MyClass()
print(a.i)
print(MyClass.i)
b = MyClass(789)
print(b.i)
