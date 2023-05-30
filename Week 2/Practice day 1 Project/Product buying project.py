class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    
    def __repr__(self) -> str:
        return f'{self.name}: {self.price}TK'

class Shop:

    def __init__(self, name) -> None:
        self.name = name
        self.items = []

    def add_product(self, product_name):
        self.items.append(product_name)

    def buy_product(self, product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f'Congress! You bought {item.name}, price: {item.price}TK.')
                return
        print(f'Sorry, {product_name} is not available.')

    def __repr__(self) -> str:
        return f"Shop name: {self.name}\nProduct: {', '.join(str(item) for item in self.items)}"

shop = Shop('Fruits shop')

Product1 = Product('Mango', 10)
Product2 = Product('Pineapple', 30)
Product3 = Product('Jack fruits', 150)

shop.add_product(Product1)
shop.add_product(Product2)
shop.add_product(Product3)

print(shop)

shop.buy_product('Mango')

