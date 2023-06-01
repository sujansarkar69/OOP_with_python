"""
static attribute: (class attribute)
statice method: @staticmethod
class method: @classmethod
"""

class Shopping:
    cart = [] # class attribute/ static attribute
    origin = 'china'

    def __init__(self, name, location) -> None:
        self.name = 'jamu na' # instance attribute

    def purchase(self, item, price, amount): # instance method
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}')

    @staticmethod
    def mul(a, b):
        print(a * b)


    @classmethod
    def hudai_dekhi(self, item):
        print('Hudai dekhte ashchi AC r hawa khaite', item)


# Shopping.purchase('Bashundara', 'lungi', 500, 1000) 
pur = Shopping('DIOR', 'Banasree')
pur.purchase('lungi', 500, 1000)

# Class method
Shopping.hudai_dekhi('Lungi')

# Statice method
Shopping.mul(4, 4)