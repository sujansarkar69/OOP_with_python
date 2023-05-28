class Shop:

    def __init__(self, buyer):
        self.buyer = buyer 
        self.cart = [] # this is instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)

sujaan = Shop('Sujan Sarkar')
sujaan.add_to_cart('Shoes')
sujaan.add_to_cart('Phone')
sujaan.add_to_cart('something else')

print(sujaan.cart)

xyz = Shop('XYZ')
xyz.add_to_cart('Cap')
xyz.add_to_cart('watch')
print(xyz.cart)