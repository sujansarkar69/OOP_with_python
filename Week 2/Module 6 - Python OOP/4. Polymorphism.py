"""
Poly --> many(multiple)
morph --> shape 
"""

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print('Making sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Meow meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('Gheu gheu')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Beh beh')

tiger = Cat('Tiger')
tiger.make_sound()

lion = Dog('Lion')
lion.make_sound()

mess = Goat("L M")
mess.make_sound()

Animals = [tiger, lion, mess]
for animal in Animals:
    print(animal.make_sound())

