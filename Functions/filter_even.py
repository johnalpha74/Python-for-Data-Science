def filter_even_numbers(number_list):
    result_list = []
    for number in number_list:
        if number % 2 == 0:
            result_list.append(number)
            return result_list


even_list = filter_even_numbers([1, 2, 3, 4,5, 6, 7, 8, 9, 10])


filter_even_numbers([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(filter_even_numbers(even_list))
