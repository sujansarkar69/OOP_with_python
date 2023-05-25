# list --> []
# tuple --> ()
# set --> {}

# set: unique items collection (no duplicate)
numbers = [3, 4, 2, 56, 23, 123, 45, 67, 86, 56, 76, 67, 2]
print(numbers)
numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(50)
numbers_set.remove(4)
print(numbers_set)

A = {1, 3, 5, 7}
B = {1, 2, 3, 4, 5}
print(A & B) 
print(A | B) # AUB
