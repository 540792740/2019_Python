class Animal:
    def __init__(self):
        self.name = 'animal'

    def eat(self):
        print('eat...')

    def sleep(self):
        print('sleep....')


class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def bark(self):
        print('Bark....')

class Cat(Animal):
    def catch(self):
        print('catch')


d1 = Dog('dog_init')
d1.sleep()
print(d1.name)