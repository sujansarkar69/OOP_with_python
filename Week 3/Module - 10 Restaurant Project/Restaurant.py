class Restaurant:
    def __init__(self, name, rent, menu = []) -> None:
        self.name = name
        self.chef = None
        self.server = None
        self.manager = None
        self.order = []
        self.rent = rent
        self.menu = menu
        self.profit = 0
        self.balance = 0
        self.expense = 0
        self.revenue = 0
        
    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server = employee
        elif employee_type == 'manager':
            self.manager = employee
    
    def receive_payment(self, order, amount, customer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            print('Not enough money! pay more.')
        
    def add_orders(self, order):
        self.order.append(order)
        
    def pay_expense(self, amount, description):
        if amount < self.balance:
            self.expense += amount
            self.balance -= amount
            print(f'Expense {amount} for {description}')
        else:
            print(f'Not enough money to pay {amount}')

    def pay_salary(self, employee):
        print(f'Paying salary for {employee.name}, salary: {employee.salary}')
        if employee.salary < self.balance:
            self.balance -= employee.salary
            self.expense += employee.salary
            employee.receive_salary()

    def show_employee(self):
        print(f"{'-' * 7} SHOWING EMPLOYEE{'-' * 7}")
        if self.chef is not None:
            print(f'Chef: {self.chef.name} with salary: {self.chef.salary}')
        if self.server is not None:
            print(f'Server: {self.server.name} with salary: {self.server.salary}')
        if self.manager is not None:
            print(f'Manager: {self.manager.name} with salary: {self.manager.salary}')
            

