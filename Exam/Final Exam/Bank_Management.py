class Person:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        self.balance = 0


class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.balance = 0
        self.loan = True
        self.loan_balance = 0

    def Can_give_loan(self, amount):
        if self.loan == True:
            if amount < self.balance:
                self.loan_balance += amount
                return True
        else:
            return False

    def loan_feature(self):
        if self.loan == True:
            self.loan = False
            return False
        else:
            self.loan = True
            return True


class User:
    users_account = {}
    id = 1

    def __init__(self, bank) -> None:
        self.bank = bank
        self.name = None
        self.email = None
        self.password = None
        self.id = None
        self.balance = 0
        self.transaction_history = []

    def create_account(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.id = User.id
        User.id += 1
        user = Person(email, password)
        self.users_account[self.id] = (vars(user))

    # User can Deposite and withdraw amount
    def deposite_amount(self, amount):
        if amount > 0:
            self.balance += amount
            self.bank.balance += amount
            print(f'${amount} Deposite Successful!')
            self.transaction_history.append(f'Deposite: +${amount}')
            if self.id in self.users_account:
                user = self.users_account[self.id]
                user['balance'] = self.balance
        else:
            print(f'Can not Deposite balance: ${amount}')

    def withdraw(self,  amount):
        if amount <= self.balance:
            self.balance -= amount
            self.bank.balance -= amount
            print(f'${amount} Withdraw Successful!')
            self.transaction_history.append(f'Withdrawal: ${amount}')
            if self.id in self.users_account:
                user = self.users_account[self.id]
                user['balance'] = self.balance
        else:
            print(f"Balance ${amount} is not available in your account")

    # User can check his balances
    def check_balance(self):
        print(f"your balance: ${self.users_account[self.id]['balance']}")

    # User can transfer the amount from his account ot another account
    def transfer(self, transfer_account, amount):
        if transfer_account in self.users_account:
            if self.balance >= amount:
                print(f"${amount} Transfer Successful!")
                self.transaction_history.append(
                    f'Transaction to account {transfer_account}: -${amount}')
                self.users_account[self.id]['balance'] -= amount
                self.balance -= amount
                self.users_account[transfer_account]['balance'] += amount
            else:
                print(f"Balance ${amount} is not available in your account")
        else:
            print('Account is not available.')

    # User can check his transcation history
    def Show_transaction_history(self):
        print(f"{'-' * 10} Transaction History {'-' * 10}")
        for trans in self.transaction_history:
            print(trans)

    # User can take a loan from the bank
    def take_loan(self, amount):
        # Given that can loan from the bank twice of total amount
        loan_lim = self.users_account[self.id]['balance'] * 2
        if amount < loan_lim:
            if self.bank.Can_give_loan(amount):
                self.balance += amount
                print(f"${amount} Loan got Successful!")
                self.transaction_history.append(f"Loan: +${loan_lim}")
                if self.id in self.users_account:
                    user = self.users_account[self.id]
                    user['balance'] = self.balance
            else:
                print('Loan feature is off currently.')
        else:
            print(f"Loan limit reached.")


class Admin:
    admin_accounts = {}
    id = 478801

    def __init__(self, bank) -> None:
        self.bank = bank
        self.name = None
        self.email = None
        self.password = None
        self.id = None

    def create_account(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.id = Admin.id
        Admin.id += 1
        admin = Person(email, password)
        self.admin_accounts[self.id] = (vars(admin))

    def check_bank_balance(self):
        print(f'Bank Balance: ${self.bank.balance}.')

    def check_loan_amount(self):
        print(f'Total loan: ${self.bank.loan_balance}.')

    def loan_feature(self):
        if self.bank.loan_feature():
            print('Loan feature on.')
        else:
            print('Loan feature off.')


# Creating Bank
bank = Bank('Islami Bank')

# users create account:
user = User(bank)
user.create_account('Sujan Sarkar', 'user.@gmail.com', 'password123')
user1 = User(bank)
user1.create_account('Seeam Sarkar', 'user1.@gmail.com', 'password1234')

# admin account:
admin = Admin(bank)
admin.create_account('Mahfuz', 'mahfuz@gmail.com', 'admin123')

# deposit money:
user.deposite_amount(2352)
user1.deposite_amount(2543)
user.check_balance()
user1.check_balance()

# withdraw money:
user.withdraw(500)
user1.withdraw(500)
user.check_balance()
user1.check_balance()

# transfer money:
user.transfer(2, 200)
user1.transfer(1, 400)
user.check_balance()
user1.check_balance()

# take loan:
user.take_loan(5000)
user1.take_loan(1000)
user.check_balance()
user1.check_balance()


# admin check bank balance:
admin.check_bank_balance()

# admin check total loan amount:
admin.check_loan_amount()

# loan feature off on by admin:
admin.loan_feature()

# Transaction history:
user.Show_transaction_history()
user1.Show_transaction_history()