"""
Q -> Explain with proper examples what is meant by polymorphism in Python.

A -> Poly means many or multiple and morph means shape or forms so polymorphism means the condition
of occurring in several different forms. In Object Oriented Programming,
that’s exactly what the fourth and final pillar is concerned with - types in the same inheritance chains being able to do different things.

Let’s explain through an example:

import math
class Shape:
    def __init__(self, name) -> None:
        self.name = name

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, name, radius) -> None:
        self.radius = radius
        super().__init__(name)
    
    def area(self):
        return math.pi * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)
    
    def area(self):
        return self.length * self.width

shape = Shape('Shape')

Circle_area = Circle('Circle', 2)
print(Circle_area.area())

Rectangle_area = Rectangle('4 shape', 3, 4)
print(Rectangle_area.area())

In this example, Shape class defines its name and a function called area() method
that is overridden in the derived classes Rectangle and Circle. By passing different
objects of Rectangle and Circle classes, we achieve polymorphic behavior 
where the appropriate area() method is called based on the type of the object.
"""
import math
class Shape:
    def __init__(self, name) -> None:
        self.name = name

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, name, radius) -> None:
        self.radius = radius
        super().__init__(name)
    
    def area(self):
        return math.pi * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)
    
    def area(self):
        return self.length * self.width

shape = Shape('Shape')

Circle_area = Circle('Circle', 2)
print(Circle_area.area())

Rectangle_area = Rectangle('4 shape', 3, 4)
print(Rectangle_area.area())