"""
Encapsulation : hide details
access modifier: Public, Protected, Private
"""

class Bank:
    def __init__(self, holder_name, initail_deposit) -> None:
        self.holder_name = holder_name
        self._brance = 'banani 11' # Protected attribute
        # self.balance = initail_deposit # Public attribute
        self.__balance = initail_deposit # Private attribute

    def deposite(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
rafsan = Bank('Rafsan bro', 10000)
print(rafsan.holder_name)
# print(rafsan.__balance)
rafsan.deposite(40000)
print(rafsan.get_balance())
# print(rafsan._brance)
# print(dir(rafsan))
print(rafsan._Bank__balance)
    