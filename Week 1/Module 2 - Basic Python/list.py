# array, list, collection is same (simple terms)

# index =   0   1   2   3   4   5   6   7   8   9   10 //Positive index 
numbers = [23, 45, 34, 21, 56, 93, 84, 73, 61, 50, 39]
# index =  -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1  //Negative index

print(numbers[3], numbers[-3])
# list( start : end ) //start from the start index and stops before the end index
print(numbers[1:4])

# list( start : end: step )
print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[1:7:-1])
print(numbers[7:1:-1])
print(numbers[3:])
print(numbers[:6])
print(numbers[:]) # shortcut to copy a list
print(numbers[::-1]) # shortcut to reverse a list