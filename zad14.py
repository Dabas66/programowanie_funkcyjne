def count_unique_elements(input_list):
    unique_elements = set(input_list)
    return len(unique_elements)

my_list = [11,22,11,22,33]
result = count_unique_elements(my_list)
print(result)
