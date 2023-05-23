# defalut args
def full_name(first, last):
    name = f'Full Name: {first} {last}'
    return name

# take parameters in order(serial wise)
# name = full_name('Sujan','Sarkar')
name = full_name(last= 'Sarkar',first='Sujan')
print(name)

# kargs (key args) ->
def famous_name(first, last, **addition):
    name = f'full name: {first} {last}'
    # print(addition)
    print(addition['goal'])
    for key, value in addition.items():
        print(key, value)
    return name

name = famous_name(first= 'Sujan', last= 'Sarkar', title= 'Student',goal1='Future Engineer', goal='tech giants')
print(name)

# return multiple things from an array
def a_lot(num1 , num2):
    sum = num1 + num2
    mul = num1 * num2
    remain = num1 - num2
    # return [sum, mul, remain]
    return sum, mul, remain

everything = a_lot(32, 44)
print(everything)