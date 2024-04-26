# Boolean Operators

# Python Program to demonstrate
# the OR operator

number_one = 3
number_two = 5
number_three = 8

print(number_one, number_two, number_three)
if number_one > number_two or number_two > number_three:
    print(True)
else:
    print(False)

print("None of the numbers has the boolean value: True")

# Python Program to demonstrate
# the AND operator

number_one = 4
number_two = 6
number_three = 7

print(number_one, number_two, number_three)
if  number_one < number_two and number_three < number_two:
    print(False)
else:
    print(True)
