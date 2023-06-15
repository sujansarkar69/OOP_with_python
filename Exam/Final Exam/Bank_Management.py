class User:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password

class Login:
    def __init__(self) -> None:
        self.users = []
        self.accounts = {}
        self.balance = 0
        self.loan = True
        self.loan_balance= 0

    def bank(self):
        self.accounts = {}
        self.balance = 0
        self.loan = True
        self.loan_balance= 0
    
    # 1. User and Admin create account
    def create_account(self, email, password, is_admin = False):
        user = User(email, password)
        self.users.append((user, is_admin))
        account = len(self.users)
        self.accounts[account] = {'name': email, 'balance': 0, 'loan_amount': 0, 'loan_limit': 0, 'transaction_history': []}
        print('Account Created Successful!')
        return account
    
    
    
    # 2. User can Deposite and withdraw amount
    def deposite_amount(self, account, amount):
        if amount > 0:
            self.accounts[account]['balance'] += amount
            self.balance += amount
            self.accounts[account]['transaction_history'].append(f'Deposite: +${amount}')
            print('Deposite Successful!')
        else:
            print(f'Can not Deposite balance: ${amount}')


    def withdraw(self, account, amount):
        if amount > 0:
            if amount <= self.accounts[account]['balance']:
                self.accounts[account]['balance'] -= amount
                self.accounts[account]['transaction_history'].append(f'Withdrawal: -${amount}')
                print('Withdraw Successful!')
            else:
                print(f"Balance ${amount} is not available in your account")

    # 3. User can check his balances
    def check_balance(self, account):
        print(f"your balance: ${self.accounts[account]['balance']}")

    # 4. User can transfer the amount from his account ot another account
    def transfer(self, my_account, transfer_account, amount):
        if my_account in self.accounts and transfer_account in self.accounts:
            sender = self.accounts[my_account]['balance']
            if sender >= amount:
                self.accounts[my_account]['balance'] -= amount
                self.accounts[transfer_account]['balance'] += amount
                self.accounts[my_account]['transaction_history'].append(f'Transaction to account {transfer_account}: -${amount}')
                self.accounts[transfer_account]['transaction_history'].append(f'Transaction from account {my_account}: +${amount}')
                print(f"${amount} Transfer Successful!")
            else:
                 print(f"Balance ${amount} is not available in your account")
        else:
            print('Account is not available.')
            
    # 5. User can check his transcation history 
    def transaction_history(self, account):
        if account in self.accounts:
            history = self.accounts[account]['transaction_history']
            print(f"{'-' * 10} Transaction History {'-' * 10}")
            for trans in history:
                print(trans)

    # 6. User can take a loan from the bank
    def take_loan(self, account):
        if account in self.accounts:
            if self.loan == True:
                acnt = self.accounts[account]
                loan_lim = acnt['balance'] * 2 # Given that can loan from the bank twice of total amount
                if loan_lim > acnt['loan_limit']:
                    acnt['loan_limit'] = loan_lim
                    acnt['loan_amount'] += loan_lim
                    self.loan_balance += loan_lim
                    acnt['transaction_history'].append(f"Loan: +${loan_lim}")
                    print(f"${loan_lim} Loan Successful!")
                else:
                    print(f"Loan limit reached.")
            else:
                print('Loan feature is off currently.')
        else:
            print('Account is not available.')

    # Admin can check total bank balances
    def bank_balance(self):
        print(f'total bank balace: ${self.balance}')
    
    # Admin can check the total loan amount
    def check_total_loan(self):
        print(f"Your Loan amount is: ${self.loan_balance}")

    # user and admin login 
    def Log_in(self, email, password):
        for index, (user, is_admin) in enumerate(self.users):
            if user.email == email and user.password == password:
                if is_admin:
                    print(f"{'-' * 10} Admin {'-' * 10}")
                    print('1. Check Balance.\n2. Check Loan amount.\n3. Off Loan feature')
                    user_input = int(input('Press your option: '))
                    if user_input == 1:
                        self.bank_balance() # admin check bank balance
                    elif user_input == 2:
                        self.check_total_loan() # admin check total loan
                    elif user_input == 3:
                        wanna_off = input('Press Y for off and N for don\'t off: ')
                        if wanna_off == 'Y':
                            self.loan = False # disable loan feature 
                            print('Loan feature off Successfully!')
                        elif wanna_off == 'N':
                            self.loan = True
                    else:
                        print("Invalid Option.")
                else:
                    account = index + 1
                    print('1. Check Balance.\n2. Deposite Amount.\n3. Withdraw Amount.\n4. Transfer Amount.\n5. Check Transaction history.\n6. Take a loan.')
                    user_input = int(input('Press your option: '))
                    if user_input == 1:
                        self.check_balance(account)
                    elif user_input == 2:
                        amount = float(input('Deposite Amount: '))
                        self.deposite_amount(account, amount)
                    elif user_input == 3:
                        amount = float(input('Withdraw Amount: '))
                        self.withdraw(account, amount)
                    elif user_input == 4:
                        transfer_account = int(input('transfer account number: '))
                        amount = int(input('Transfer amount: '))
                        self.transfer(account, transfer_account, amount)
                    elif user_input == 5:
                        self.transaction_history(account)
                    elif user_input == 6:
                        self.take_loan(account)
                    else:
                        print('Invalid Option.')
                return
        print('Invalid email or password! try again.')

login = Login()

while True:
    print(f"{'-' * 10} BANK MANAGEMENT SYSTEM {'-' * 10}")
    print('1. Sing in.\n2. Sing up.')
    user_input = int(input('Press: '))
    if user_input == 1:
        print('Sing in page: ')
        email = input('Enter email: ')
        password = input('Enter password: ')
        login.Log_in(email, password)
    elif user_input == 2:
        print('Sing up page: ')
        email = input('Enter email: ')
        password = input('Enter password: ')
        user_type = int(input('1. Admin.\n2. User.\nPress: '))
        if user_type == 1:
            login.create_account(email, password, is_admin= True)
        elif user_type == 2:
            login.create_account(email, password, is_admin=False)
        else:
            print('Invalid user type!')
    else: 
        print('Invalid Option.')
    
    continuee = input('Wanna exit? Press Y or exit otherwise press anything to continue: ')
    if continuee == 'Y':
        break
    