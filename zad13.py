def split_list(input_list, chunk_size):
    return [input_list[i:i+chunk_size] for i in range(0, len(input_list), chunk_size)]


my_list = [9, 9, 9, 9, 9, 7, 9, 9, 8, 100]
result = split_list(my_list, 3)
print(result)
