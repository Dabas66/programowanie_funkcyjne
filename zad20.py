def sum_of_squares_of_odds(input_list):
    return sum(x**2 for x in input_list if x % 2 != 0)


my_list = [2,4,6,8,9,3,1]
result = sum_of_squares_of_odds(my_list)
print(result)
