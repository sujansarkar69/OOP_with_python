"""
Q -> Write the advantages of using inner functions in Python OOP. Provide specific 
use cases where inner functions can enhance code readability and organization. 
(note: answer with proper examples).

A ->

A Function defined inside another function is an inner function. 
- Advantages of using an inner function:
- Provide encapsulation by nesting functions in other functions
- Implement closure factory functions that retain state between calls
- Build decorator functions to provide new functionalities

Specific use cases:
Encapsulation: A function can be created as an inner function in order to protect it from everything that is happening outside 
of the function. In that case, the function will be hidden from the global scope. Here is an example:
def outer_func(num):
    def inner_func(num):
        return num * 2
    num2 = inner_func(num)
    print(num, num2)
inner_func(5)
In this example, we are trying to call inner_func(), but instead we got an error. But if we call the outer_func() 
then it will work as well.So, the inner function is protected from what is happening outside and is not affected 
by the value passed to the parameter num of the outer function. The variables inside the inner function is not accessible outside it. 
After checking all arguments in the outer function, we can safely skip error checking within the inner function.

Organization and code reuse: Inner functions can help organize code by grouping related functionality together.
They can also be used for code reuse within a specific method, avoiding code duplication and improving maintainability.
class ReportGenerator:
    def generate_report(self, data):
        def format_data():
            pass

        def generate_header(): 
            pass

        def generate_body():
            pass

        def generate_footer():
            pass

        format_data()
        generate_header()
        generate_body()
        generate_footer()

The example demonstrates how inner functions can be used within the "generate_report" method of a class to organize code and 
improve code reuse. Each inner function handles a specific task related to report generation, promoting modularity and 
facilitating maintenance and modifications in the future.

Closures and factory Function: Closures are powerful constructs in programming that allow inner functions to retain access to the 
scope of their enclosing functions even after the outer functions have finished executing. For example, have a look at the code:
def get_discounted_price(price):
    def discounted_price(discount):
        return price * discount
    return discounted_price

first_discount = get_discounted_price(10)
second_discount = get_discounted_price(10)
# print (first_discount(0.50))
# print (second_discount(0.60))

In this example, the outer function get_discounted_price returns a reference to the inner function discounted_price. 
This inner function, when called later as first_discount and second_discount, still has access to the price variable from 
its enclosing scope. This enables the inner functions to calculate the discounted price using the supplied discount values. 
Closures are commonly used to maintain the state of a function, making them valuable in various programming scenarios.

Inner function helps us in defining the factory function. A factory function is a function that creates another object. For example:
def find_pow(num):
    def pow_n(power):
        return num ** power
    return pow_n

power_of_2 = find_pow(2)
print(power_of_2(3))
In this code, The power_n(power) function acts as a factory function, generating the power_of_2 function based on the parameter 
we provide.


"""

def outer_func(num):
    def inner_func(num):
        return num * 2
    num2 = inner_func(num)
    print(num, num2)
outer_func(5)

def get_discounted_price(price):
    def discounted_price(discount):
        return price * discount
    return discounted_price

first_discount = get_discounted_price(10)
second_discount = get_discounted_price(10)
# print (first_discount(0.50))
# print (second_discount(0.60))

def find_pow(num):
    def pow_n(power):
        return num ** power
    return pow_n

power_of_2 = find_pow(2)
print(power_of_2(3))


class ReportGenerator:
    def generate_report(self, data):
        def format_data():
            pass

        def generate_header(): 
            pass

        def generate_body():
            pass

        def generate_footer():
            pass

        format_data()
        generate_header()
        generate_body()
        generate_footer()
