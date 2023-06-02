# Multi-level inheritance: Grandpa --> parent --> child
"""
Q -> Explain with proper examples what is meant by multilevel inheritance in Python.

A -> 
Base class or Parent class to Derived class or child class and Derived class to derived class is called Multi-level inheritance.

An easy way to explain: Grandpa to parent and parent to child.
Let’s explain through an example:

class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f'{self.name}, {self.price}'
    
class Bus(Vehicle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat
        super().__init__(name, price)


class ACBus(Bus):
    def __init__(self, name, price, seat, temparature) -> None:
        self.temparature = temparature
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        print(f'temp: {self.temparature}, seat: {self.seat}')
        return super().__repr__()
    
green_line = ACBus('GLine', 5000000, 32, '+20 to -20')
print(green_line)
In this example, there are three classes: Vehicle, Bus, ACBus, they representing a hierarchy of multi-level inheritance. The Vehicle class serves as the base class. It has attributes for name and price and provides a string representation of the object. The Bus class is derived from the Vehicle class and adds an attribute for the number of seats in the bus. It initializes the inherited attributes and provides access to the base class's string representation. The ACBus class is derived from Bus and introduces an additional attribute for temperature range. It initializes the inherited attributes and overrides the string representation method to include the temperature and seat attributes.

Thus, multi-level inheritance allows for a hierarchy of classes, where each derived class inherits the characteristics of its immediate parent class and can further extend or modify those characteristics as needed.


"""

class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f'{self.name}, {self.price}'
    
class Bus(Vehicle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat
        super().__init__(name, price)


class ACBus(Bus):
    def __init__(self, name, price, seat, temparature) -> None:
        self.temparature = temparature
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        print(f'temp: {self.temparature}, seat: {self.seat}')
        return super().__repr__()
    
green_line = ACBus('GLine', 5000000, 32, '+20 to -20')
print(green_line)