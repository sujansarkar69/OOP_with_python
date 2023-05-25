# lambda function

# def doubled(n):
#     return n*2

doubled = lambda n : n * 2
result = doubled(44)
# print(result)

numbers = [3, 4, 2, 56, 23, 123, 45, 67, 86, 56, 76, 67, 2]
doubled_nums = map(doubled, numbers)
# print(doubled_nums)
# print(numbers)
# print(list(doubled_nums))

suqared_nums = map(lambda x: x * x, numbers)
# print(list(suqared_nums))

CS_student = [
    {'Name': 'Sujan', 'Age': 20},
    {'Name': 'Seyam', 'Age': 24},
    {'Name': 'Shahadat', 'Age': 21},
    {'Name': 'Rakib', 'Age': 18},
    {'Name': 'Mohin', 'Age': 17},
    {'Name': 'Naim', 'Age': 17},
]

juniors = filter(lambda junior : junior['Age'] < 20, CS_student)
print(list(juniors))