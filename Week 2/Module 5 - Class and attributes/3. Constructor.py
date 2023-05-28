class Phone:
    manufacturer = 'China'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def sms_send(self, phone, sms):
        text = f"Sending SMS to: {phone}, and message: {sms}"
        return text

my_phone = Phone('Me', 'iPhone', 85000)
print('Brand:',my_phone.brand,', Price:',my_phone.price)

her_phone = Phone('X', 'Samsung', 120000)
print('Brand:',her_phone.brand,', Price:',her_phone.price)