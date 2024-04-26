# Python general practice

# Reverse the order of elements in a list
my_list = ['John', 'Alpha', 'Code', 'Brewers', 'Bootcamp', 'Founder']
my_fruit_list = ['Oranges', 'Cherries', 'Mangoes']
my_list.reverse()
print("\nThe reversed elements of the list are: " + str(my_list))

# Add elements to a lsit in Python
# Appending method adds at the back of the list
my_list.append('Midrand')
print("\nThe list with appended elements" + str(my_list))

# Using insert method
# Inserting method inserts at a given index of the list
my_list.insert(1, 'South Africa')
print("\nThe list with inserted elements:" + str(my_list))

# Adding elements of the two lists
new_list = my_list + my_fruit_list
print("\nThe new list is: " + str(new_list))

# Sorting a list of strings in alphabetical order
my_list.sort()
print("\nThe sorted list in alphabetical order is below: \n" + str(my_list))

# Sorting a lsit in reverse order
my_fruit_list.sort(reverse=True)
print("\nThe reversed list is: \n" + str(my_fruit_list))



