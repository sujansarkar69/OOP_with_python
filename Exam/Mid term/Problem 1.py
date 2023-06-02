"""
Q -> Write down the differences between class method and static method of Python with proper examples.(at least 3)		

A ->
Differences between a class method and a static method:

Class method: 
Class methods can access the class and can modify class-level variables and attributes. 
The class method takes his class parameter first called self.
The class method uses @classmethod decorator for a class method
Example:
class class_Method:
    class_attribute = []
    class_attribute1 = 'this is attribute'
    @classmethod # we use this decorator for class method 
    def canAccess(self, other): # in first parameter class method takes his class method
        print(f'{self.class_attribute}, {self.class_attribute1}, {other}') # class method can access the class state
test = class_Method()
test.canAccess('class can access class attributes')


Static method:
Static methods can not access the class and can’t modify anything.
Static methods don’t take any specific parameter.
Static methods use @staticmethod decorator for a static method.
Example:
class Static_method:
    class_attribute = []
    class_attribute1 = 'this is attribute'
    @staticmethod # we use this decorator for static method
    def canAccess(self, other): # don't take any specific parameter
        print(f'{self}, {other}') # static method can not access the class state
test = Static_method()
test.canAccess('class can access class attributes')


"""



class class_Method:
    class_attribute = []
    class_attribute1 = 'this is attribute'
    @classmethod # we use this decorator for class method 
    def canAccess(self, other): # in first parameter class method takes his class method
        print(f'{self.class_attribute}, {self.class_attribute1}, {other}') # class method can access the class state
test = class_Method()
test.canAccess('class can access class attributes')

class Static_method:
    class_attribute = []
    class_attribute1 = 'this is attribute'
    @staticmethod # we use this decorator for static method
    def canAccess(self, other): # don't take any specific parameter
        print(f'{self}, {other}') # static method can not access the class state
test = Static_method()
test.canAccess('class can access class attributes')