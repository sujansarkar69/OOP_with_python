from Menuu import *
from Restaurant import *
from User import *
from Orderr import *
def main():
    menu = Menu()

    # Add pizza to the menu
    pizza1 = Pizza('Shutki pizza', 800, 'large', ['Shutki', 'onio'])
    menu.add_items('pizza', pizza1)
    pizza2 = Pizza('alu vorta pizza', 400, 'large', ['potato', 'onio'])
    menu.add_items('pizza', pizza2)
    pizza3 = Pizza('dal pizza', 400, 'large', ['dal', 'onio', 'oil'])
    menu.add_items('pizza', pizza3)

    # Add burger to the menu
    burger1 = Burger('Naga burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_items('burger', burger1)
    burger2 = Burger('beef burger', 1200, 'beef', ['beef','bread'])
    menu.add_items('burger',burger2)

    # add drinks to the menu
    coke = Drinks('coca-cola', 400, True)
    menu.add_items('drinks', coke)
    coffee = Drinks('mocha', 1200, True)
    menu.add_items('drinks', coffee)
    
    # Showing menu
    # menu.show_menu()

    restaurant = Restaurant('Kacchi dine', 2000, menu)

    manager = Manager('Sujan Sarkar', 1234, 'sujan@sarkar.com', 'comilla', 3000, 'jan - 1 - 2020', 'core')
    restaurant.add_employee('manager', manager)

    chef = Chef('Seyam', 234, 'seyam@hossen.come', 'kotbari', 2300, 'jan 2 2020', 'chef', 'everything')
    restaurant.add_employee('chef', chef)

    server = Server('Rustom', 365, 'rustom.com', 'kandir', 1200, 'feb 2 2021', 'serve')
    restaurant.add_employee('server', server)

    # Showing employees
    # restaurant.show_employee()

    # Customer 1 placing an order
    customer1 = Customer('Tamim', 654, 'tamim@khan.com', 'bolbo na', 100000)
    order1 = Order(customer1, [pizza3, coke, burger2])
    customer1.place_order(order1)
    restaurant.add_orders(order1)

    # Customer 1 paying for order1
    restaurant.receive_payment(order1, 2000, customer1)
    print('revenue and balance after first customer: ',restaurant.revenue, restaurant.balance)

    # Customer 2 placing an order2
    customer2 = Customer('kalachan', 654, 'kala@chan.com', 'bolbo na', 100000)
    order2 = Order(customer2, [pizza3, coffee, burger2])
    customer2.place_order(order2)
    restaurant.add_orders(order2)

    # Customer 2 paying for order2
    restaurant.receive_payment(order1, 2000, customer1)
    print('revenue and balance after second customer: ',restaurant.revenue, restaurant.balance)

    # pay rent
    restaurant.pay_expense(restaurant.rent, 'Rent')
    print('after rant: ', restaurant.revenue, restaurant.balance, restaurant.expense)

    # pay salary
    restaurant.pay_salary(server)
    print('after salary: ', restaurant.revenue, restaurant.balance, restaurant.expense)


if __name__ == '__main__':
    main()