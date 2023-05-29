# Base class, parent class, common attribute + functionality class
# derived class, child class, uncommon attribute + functionlaity class

class Gadget:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    
    def run(self):
        return f'Running: {self.brand}'
        
class Laptop:
    def __init__(self, memory) -> None:
        self.memory = memory
    
    def coding(self):
        return f'Learing python and practicing'
    
class Phone(Gadget):
    def __init__(self, brand, price, color, origin, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin) # Super class for inherite parent class/ common class/ base class

    def phone_call(self, number, text):
        return f'Sending SMS to: {number} with {text}'
    
    def __repr__(self) -> str:
        return f'Phone: {self.brand}, price: {self.price}, color: {self.color}, dual sim: {self.dual_sim}'
    
class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def lens(self):
        pass

# inheritance 
my_phone = Phone('iPhone', 120000, 'Silver', 'China' ,'True')
my_phone.brand
print(my_phone)