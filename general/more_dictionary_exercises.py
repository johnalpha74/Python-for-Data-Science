# Restrictions on Dictionary Keya and Values in Python
# What happens when you use the same key multiple times
car_details = {
    'model': 'Toyota',
    'body Type': 'Sedan',
    'year': 2022,
    'country': 'South Africa',
    'year': 2023,
    'country': 'Zimbabwe'
}
# The second occurrence of the key overrides the first occurrence of the key
# A key cannot be used twice in a dictionary
# Duplicate keys are not allowed
# Neither a list or a key can be a dictionary itself in Python
# Keys of a dictionary can be an immutable data type
print(car_details)

# Can you create a copy of the dictionary without modifying the original copy?
car_details_copy = car_details.copy()
car_details_copy.pop('year')
print(car_details_copy)
car_details_copy.get('1', 'colour')
print(car_details_copy)

# Adding the key value pairs to another dictionary using update method
car_details_new = {
    'Manufacturer': 'Japan',
}

print(car_details_new)
car_details_new.update(car_details_copy)
print(car_details_new)
