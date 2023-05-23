# Default args ->
# def sum(num1, num2):
#     result = num1 + num2
#     print('sum : ',result)

# sum(40, 39)

# *args (star args)->
def all_sum(*args):
    sum = 0
    print(args)
    for num in args:
        sum += num
    return sum

total = all_sum(20, 10, 3, 4)
print('all sum: ', total)

