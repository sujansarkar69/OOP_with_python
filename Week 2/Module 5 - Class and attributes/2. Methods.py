def call():
    print("callling some person")
    return 'call done'


class Phone:
    price = 86000
    color = 'white'
    brand = 'iPhone'

    def call(self):
        print('calling one person')

    def sms_send(self, phone, sms):
        text = f"Sending SMS to: {phone}, and message: {sms}"
        return text


my_phone = Phone()
print(my_phone)
print(my_phone.brand)
my_phone.call()

result = my_phone.sms_send(23423,'Sorry I forgot to missed you')
print(result)