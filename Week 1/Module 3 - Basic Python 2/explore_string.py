name = 'Sujan\'s sarkar' # escpae -> \
name1 = "sujan sarkar"
# Multiline string
name2 = """sujan sarkar
future software engineer.
"""
print(name)
print(name1)
print(name2)

# string is a sequence of characters
for char in name1:
    print(char)

print(name[2:7])
print(name[::-1])

# mutable means changeable
# immutable means you can not change it
# name[0] = 'R'
print(name)
print(name1.capitalize())
print(name2.capitalize())

if 'sarkar' in name:
    print('exists.')