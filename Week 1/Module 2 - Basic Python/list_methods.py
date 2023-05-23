numbers = [23, 45, 34, 21]
numbers.append(12)
print(numbers)

numbers.insert(2, 5)
print(numbers)

if 69 in numbers:
    numbers.remove(69)
if 5 in numbers:
    numbers.remove(5)
print(numbers)
last = numbers.pop()
print(last, numbers)
sorted = numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)