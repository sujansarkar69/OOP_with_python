from abc import ABC, abstractmethod
# abc -> abstract base class

class Animal(ABC):
    @abstractmethod # enforce all derived class to have a eat method 
    def eat(self):
        print("I need Food")
    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category = 'Monkey'
        self.name = name
        super().__init__()
    
    def eat(self):
        print('Hey nana! I\'m eating banana.')

    def move(self):
        print('Hanging on the brances')

layka = Monkey('Monkey')
layka.eat()
