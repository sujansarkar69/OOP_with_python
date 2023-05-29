# Multi-level inheritance: Grandpa --> parent --> child
"""
base class to derived class and derived class to derived class is called Multi-level inheritance.

ex. (Vehicle to Bus and Bus to ACBus)

super().__init__() -> call it's parent class 
"""

class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def move(self):
        pass

    def __repr__(self) -> str:
        return f'{self.name}, {self.price}'
    
class Bus(Vehicle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat
        super().__init__(name, price)

class Truck(Vehicle):
    def __init__(self, name, price, weight) -> None:
        self.weight = weight
        super().__init__(name, price)

class PickUpTrack(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

class ACBus(Bus):
    def __init__(self, name, price, seat, temparature) -> None:
        self.temparature = temparature
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        print(f'temp: {self.temparature}, seat: {self.seat}')
        return super().__repr__()
    
green_line = ACBus('GLine', 5000000, 32, '+20 to -20')
print(green_line)