"""
Read only --> you can not set the value. value can not be changed

Gretter --> get a value of a property through a method. Most of the time, you will
get the value of a private attribute.

Setter --> set a value of a property through a method. Most of the time, you will
set the value of a private property.
"""

class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self.__age = age
        self.__money = money

    # getter without any setter is readonly attribute
    @property # getter
    def age(self):
        return self.__age
    
    #getter
    @property
    def salary(self):
        return self.__money
    
    #setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            return 'salary can not negative'
        self.__money += value
    

samsu = User('Samsu', 21, 12000)
# print(samsu.__age) # AttibuteError
# print(samsu.age()) # without getter 
print(samsu.age) # getter 
print(samsu.salary)

samsu.salary = 4500
print(samsu.salary)