# Python program to demonstrate
# Python bool() Function

# Returns False as x is not equal to y
number_one = 5
number_two = 20
print("\nPrints FALSE as " +  str(number_one) + " is not equal to " + str(number_two))
print(bool(number_one == number_two))

# Boolean value from the expression
# Prints false since number_one is not equal to number_two
print("\nPrints FALSE since " + str(number_one) + " is not equal to " + str(number_two))
print(number_one == number_two)

# Prints True since first_name is the same as surname
first_name = "John"
surname = "John"
print("\nPrints TRUE since " + str(first_name) + " is the same name as " + str(surname))
print(first_name == surname)

# Integers and Floats as Booleans
number_one = 0
print("\nPrints FALSE since the number is " + str(number_one))
print(bool(number_one))

number_two = 1
print("\nPrints TRUE since " + str(number_two) + " is above zero")
print(bool(number_two))

number_three = -9.7
print("\nPrints TRUE since " + str(number_three) + " is non-zero")
print(bool(number_three))
