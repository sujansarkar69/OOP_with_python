""" dictonary is called aslo -> 
dictonary
object
hash table
overlap with set


dic structure = {key: value, key: value}
"""

person = {'Name': 'Sujan Sarkar', 'Address': 'Cumilla', 'Age': 20, 'Profession': 'Student'}
print(person)
print(person['Name'])
del person['Age']
print(person.keys())
print(person.values())

# Special dictonary looping 
for key, value in person.items():
    print(key, ':', value)