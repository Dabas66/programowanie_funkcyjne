def sum_of_even_numbers(input_list):
    return sum(x for x in input_list if x % 2 == 0)


my_list = [4,5,3,8,1,22]
result = sum_of_even_numbers(my_list)
print(result) 
