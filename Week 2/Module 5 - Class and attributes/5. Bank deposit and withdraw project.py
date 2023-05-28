class Bank: 
    
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        # print(f'Your balance: {self.balance}tk.')
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'Gorib, you can withdraw below {self.min_withdraw}tk.')
        elif amount > self.max_withdraw:
            print(f'Borolok, bank fokir hoye jabe. you can not withdraw more than {self.max_withdraw}tk.')
        else:
            self.balance -= amount
            print(f'Here is you withdraw money: {amount}tk.')
            print(f'Your balance after withdraw: {self.get_balance()}tk.')

brac = Bank(69000)
brac.withdraw(99)
brac.withdraw(110000)
brac.withdraw(5000)
brac.deposit(10000)
print(brac.get_balance())

