# Global Scpoe:
balance = 3000

def buy_thing(item, price):
    # local scope : inside the function.
    # you can access global variable without using the global keyword
    # if you want to modify a global variable, you have to use the global keyword
    global balance
    print(f'previous balance value: ',balance)
    balance = balance - price
    print(f'balance after buying {item}: ', balance)

buy_thing('iPhone', 1000)