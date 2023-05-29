class Laptop:
    def __init__(self, brand, price, color, memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Running laptop: {self.brand}'
    
    def coding(self):
        return f'Learing python and practicing'
    
class Phone:
    def __init__(self, brand, price, color, dual_sim) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.dual_sim = dual_sim

    def run(self):
        return f'Opening phone: {self.brand}'

    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with {text}'