class Pen:
    manufacturer = 'Bangladesh'

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

my_pen = Pen('Matador - all time', 6)
print(my_pen.brand, my_pen.price)