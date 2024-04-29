def chunk_list(input_list, chunk_size):
    return [input_list[i:i+chunk_size] for i in range(0, len(input_list), chunk_size)]

my_list = [3, 2, 1, 3, -5, 5, 0, 89, 77, -90]
result = chunk_list(my_list, 3)
print(result)
