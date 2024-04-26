
# Python program to take space
# separated input as a string
# split and store it to a list
# and print the string list

members_input_string = input("Please enter names of the members: ")
split_members_list = members_input_string.split()


print("\nThe members list is: " + str(split_members_list))
print("\nThe members are: " + "\n" + str(split_members_list[0]) + "\n", str(split_members_list[1]) + "\n" + str(split_members_list[2]))

