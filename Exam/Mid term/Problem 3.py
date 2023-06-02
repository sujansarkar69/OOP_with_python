"""
->  Write a class with three instance variables a,b and c.
    - Now add the following two methods in that class 
    - sum() to get the sum of a,b and c.
    - factorial() to get the factorial of b.
"""
from math import factorial
class phitron:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b 
        self.c = c

    def sum(self):
        return self.a + self.b + self.c
    
    def factorial(self):
        fact = 1
        for i in range(1, self.b + 1):
            fact *= i
        return fact
        # return factorial(self.b) # I can find factorial using built in function

a, b, c = 4, 7, 5
test = phitron(a, b, c)
print(test.sum())
print(test.factorial())