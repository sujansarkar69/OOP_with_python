def double_decker():
    print('starting the double decker')
    def inner_fun():
        print('inside the inner')
        return 69
    return inner_fun

# print(double_decker())
# print(double_decker()())

def do_some(work):
    print('starting work')
    work()
    print('end work')

def coding():
    print('coding in python')
print(do_some(coding))