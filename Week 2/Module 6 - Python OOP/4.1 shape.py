from math import pi
class Shape:
    def __init__(self, name) -> None:
        self.name = name
    
class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, name, radius) -> None:
        self.radius = radius
        super().__init__(name)

    def area(self):
        return pi * self.radius * self.radius
    
Circle_area = Circle('britto', 5)
print(Circle_area.area())

Rectangle_area = Rectangle('Rrr', 4, 3)
print(Rectangle_area.area())