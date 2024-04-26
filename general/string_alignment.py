# String alignmentin Python
my_string_left = "|{:<10}|".format('Code')
print("\nLeft, alignment with Formatting: ")
print(my_string_left)

my_string_center = "| {:^10}|".format('Brewers')
print("\nCenter alignment with Formatting: ")
print(my_string_center)

my_string_right = "|{:>10}|".format('Bootcamp')
print("\nRight alignment with Formatting: ")
print(my_string_right)


# To demonstrate aligning of spaces
my_string = "\n{0:^20} was founded in {1:<4}!".format("CodeBrewersBootCamp",
                                                    2022)
print(my_string)
