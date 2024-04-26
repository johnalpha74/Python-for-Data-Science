# Formatting of Strings

# Default Order using the Format() method

my_string = "{} {} {}".format('T-shaped', 'Python', 'Developer')
print("The default order using the Format() method")
print(my_string)

# Positional Formatting
my_string = "{2} {0} {1}".format('T-shaped', 'Python', 'Developer')
print("\nPrint using positional order")
print(my_string)

# Keyword Formatting
my_string = "{p} {t} {d}".format(t='T-shaped', p='Python', d='Developer')
print("\nPrinting using Keyword formatting")
print(my_string)
