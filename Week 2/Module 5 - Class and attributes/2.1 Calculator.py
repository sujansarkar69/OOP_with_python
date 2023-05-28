class Calculator:
    brand = 'Casio MS990'
    def add(self, num1, num2):
        sum = num1 + num2
        return sum
    
    def deduct(self, num1, num2):
        deduct = num1 - num2
        return deduct
    
    def multiply(self, num1, num2):
        mul = num1 * num2
        return mul
    
    def divide(self, num1, num2):
        div = num1 / num2
        return div
    
my_calculator = Calculator()

sum = my_calculator.add(5, 5)
print(sum)