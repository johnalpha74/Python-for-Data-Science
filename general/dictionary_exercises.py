# A python dictionary is an unordered collection of items
# Each item has a key and a value
# Keys are used to retrieve values
# Dictionaries are created using key-value pairs
# Dictionaries store many pieces of information ina single value.

member_details = {
    'name': 'Tshepo Selelo',
    'sex': 'Male',
    'age': 32,
    'married': 'False'
}

print(member_details)
print(type(member_details))

print(member_details['name'])

# The get method is used to access values of the associated key
print(member_details.get('age'))

# The get method can also be used to accept the default value if the value is not present
print(member_details.get('address', 'not present'))

# In operator is used to find if a value is present in the dictionary
print('name' in str(member_details))
print('address' in str(member_details))

# The assignment operator is also used to change the value of keys in a dictionary
member_details['married'] = True
print(member_details['married'])

# The assignment operator is also used to a add a key-value pair
member_details['address'] = '1, William Nicol Drive'
print("\n" + str(member_details))

# The pop method can be used to remove a key-value pair
member_details.pop('age')
print("\n" + str(member_details))


# Other dictionary methods
print(member_details.keys())
print(member_details.values())
print(member_details.items())
# print(member_details.items()[1]) # Fix this error

