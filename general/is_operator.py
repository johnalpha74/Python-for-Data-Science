
# Python program to demonstrate
# is keyword

college_name_one = "CodeBrewers Bootcamp"
college_name_two = "CodeBrewers Bootcamp"

if college_name_one is college_name_two:
    print(True)
else:
    print(False)

x = ["a", "b", "c", "d"]
y = ["a", "b", "c", "d"]

print(x is y)
