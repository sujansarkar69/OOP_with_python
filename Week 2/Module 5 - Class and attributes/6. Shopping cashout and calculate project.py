class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'Item': item, 'Price': price, 'Quantity': quantity}
        self.cart.append(product)

    def remove_item(self, item):
        pass

    def checkout(self, amount):
        total = 0

        for item in self.cart:
            # print(item)
            total += item['Price'] * item['Quantity']
        print(f'Total price {total}tk.')
        if amount < total:
            print(f'Please provide {total - amount}tk more.')
        else:
            print(f'Here is your items and extra money {amount - total}tk.')

sujan = Shopping('Sujan Sakar')

sujan.add_to_cart('Alu', 25, 5)
sujan.add_to_cart('tomato', 30, 5)
sujan.add_to_cart('Meat', 750, 2)

# print(sujan.cart)

sujan.checkout(500)