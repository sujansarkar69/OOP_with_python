from datetime import date


class Bank:
    def __init__(self, name) -> None:
        self.name = name
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def given_loan(self, amount):
        if self.loan_feature_enabled:
            if amount < self.total_balance:
                self.total_loan_amount += amount
                return True
        else:
            return False

    def loan_feature(self):
        if self.loan_feature_enabled:
            self.loan_feature_enabled = False
            return False
        else:
            self.loan_feature_enabled = True
            return True


class Person:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        self.balance = 0


class User:
    store_users = {}
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
        person = Person(email, password)
        self.store_users[self.id] = (vars(person))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.bank.total_balance += amount
            print(
                f'Succesfully Deposit!!!"\n"Deposit amount is {amount} and Current balance {self.balance}')
            self.transaction_history.append(
                "Deposited is : " + str(amount) + ' by ' + str(self.name) + " date : " + str(date.today()))
            if self.id in self.store_users:
                use = self.store_users[self.id]
                use['balance'] = self.balance
        else:
            print(f'this {amount} is not possible deposit')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.bank.total_balance -= amount
            print(
                f'Successfully withdraw!!!\n Withdrew is {amount} and currently balance is {self.balance}')
            self.transaction_history.append(
                "Withdraw is : " + str(amount) + " by " + str(self.name) + " date : " + str(date.today()))
            if self.id in self.store_users:
                use = self.store_users[self.id]
                use['balance'] = self.balance
        else:
            print(f'this {amount} is not avaialbe in balance')

    def show_available_balance(self):
        print(
            f"{self.name} available balance is {self.store_users[self.id]['balance']}")

    def transfer_balance_another_account(self, account_no, amount):
        if account_no in self.store_users:
            if amount <= self.balance:
                self.transaction_history.append("transfer account id is " + str(
                    account_no) + " money -> " + str(amount) + " date : " + str(date.today()))
                self.store_users[self.id]['balance'] -= amount
                self.balance -= amount
                self.store_users[account_no]['balance'] += amount
        else:
            print("user account is not exits")

    def show_transaction_history(self):
        print("==========Transaction History==================")
        for user in self.transaction_history:
            print(user)

    def take_loan_from_bank(self, amount):
        twice_amount = self.store_users[self.id]['balance']*2
        if amount < twice_amount:
            if self.bank.given_loan(amount):
                self.balance += amount
                print(f'You got loan successfully')
                self.transaction_history.append(
                    "take Loan from bank : " + str(amount) + " date : " + str(date.today()))
                if self.id in self.store_users:
                    use = self.store_users[self.id]
                    use['balance'] = self.balance
            else:
                print(f'The curently bank loan is stopped')
        else:
            print(
                f'You can\'t take loan from bank to {amount}.you can take highest loan is {twice_amount}')


class Admin:
    store_admin = {}
    id = 501

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
        person = Person(email, password)
        self.store_admin[self.id] = (vars(person))

    def show_total_balance(self):
        print('The total avialable balance is : ',
              self.bank.total_balance, " of bank")

    def show_total_loan_amount(self):
        print('The total loan amount is : ',
              self.bank.total_loan_amount, 'of bank')

    def on_off_loanFeature(self):
        if self.bank.loan_feature():
            print('Currently loan feature is ON!!!')
        else:
            print('Currently loan feature is OFF!!!')


# Always firstly create a Bank and pass a bank name
brac_bank = Bank('brac')

# when User class use always pass a bank
# user id start from 1
user1 = User(brac_bank)
# When create account in user always pass {name,email,pass}
user1.create_account('user1', 'user1@gmail.com', 'user12345')
user2 = User(brac_bank)
user2.create_account('user2', 'user2@gmail.com', 'user2345')

# when deposti and withdraw method in user always pass a amount
user1.deposit(5000)
user1.withdraw(2000)
user1.show_available_balance()
user1.deposit(7000)
user1.withdraw(4000)
user1.show_available_balance()
# when transfer_balance_another_account method in user always pass {account_id,amount}
user1.transfer_balance_another_account(2, 1000)

# when take_loan_from_bank method in user always pass a amount
user1.take_loan_from_bank(2000)
user1.show_transaction_history()
user1.show_available_balance()
user2.show_available_balance()

# When Admin class use always pass a bank
admin = Admin(brac_bank)

# when create account in admin always pass {name, email, password}
admin.create_account('admin1', 'admin1@gmail', 'admin1234')
admin.show_total_balance()
admin.show_total_loan_amount()
admin.on_off_loanFeature()

user2.take_loan_from_bank(500)
