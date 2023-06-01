"""
Override: if the method is in parent class and also child class then it called override method

overload: 
"""

class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('vat mangso polau korma')

    def excercise(self):
        raise NotImplementedError
    
class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    # this methods 'eat' calls override 
    def eat(self):
        print('Vegetables')

    def excercise(self):
        print('GYM e taka diye gham jorai')

    # overload, +, -, * etc sign
    # + sign overload
    def __add__(self, other):
        return self.age + other.age
    # - sign overload
    def __mul__(self, other):
        return self.age * other.age
    # len overload
    def __len__(self):
        return self.height
    # > operator overload
    def __gt__(self, other):
        return self.age > other.age
    


sakib = Cricketer('Sakib Al Hasan', 38, 68, 91, 'BD')
mushfi = Cricketer('mushfi', 36, 65, 78, 'BD')
# sakib.eat()
# sakib.excercise()

# Plus sign overload
print(45 + 23)
print('Sakib' + 'moshfiq')
print([223,23,2] + [3,54 , 4 ,5])   

print(sakib + mushfi)
print(sakib * mushfi)
print(len(sakib))
print(sakib > mushfi)