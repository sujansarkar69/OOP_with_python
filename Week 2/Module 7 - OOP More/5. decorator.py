import math
import time

def timer(func):
    def inner(*args, **kwargs):
        print('time start')
        start = time.time()
        func(*args, **kwargs)
        print('time end')
        end = time.time()
        print(f'total time taken {end - start}')
    return inner

@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f'factorial {n} is: {result}')

get_factorial(1200)