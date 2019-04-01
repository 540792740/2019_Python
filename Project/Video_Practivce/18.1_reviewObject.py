class Person(object):
    num = 100
    # hh
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def shout(self):
        print(self.name)
        print(self.age)

    @classmethod
    def printnum(cls):
        print(cls.num)

    @classmethod
    def add(cls, a,b):
        return  a + b
p = Person("jw",13)
p.printnum()

print(p.add(10,9))