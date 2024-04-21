# Create a sub-string from a string by slicing it respectively from start to end
# Using a slice() method
# Syntax:
# slice(stop)
# slice(start, stop, step)

# Python program to demonstrate
# string slicing

# String Slicing
string_to_slice = 'MYSTRING'

# Using slice constructor
slice_two_characters = slice(2)
slice_a_range = slice(1, 4, 2)
slice_in_reverse = slice(-1, -8, -3)

# Slice first 2 characters
print("The first two characters of the string" + " " + string_to_slice + " " + "are:")
print(string_to_slice[slice_two_characters])

#  Slice using start and stop indecies
print(string_to_slice[slice_a_range])

# Slice in reverse
print(string_to_slice[slice_in_reverse])

# Please refactor this code later
# to use the print function for each variable
