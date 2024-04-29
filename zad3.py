def filter_even_values(input_dict):
    return {key: value for key, value in input_dict.items() if isinstance(value, int) and value % 2 == 0}

# Testowanie funkcji na przykładowym słowniku
my_dict = {'a': 66, 'b': 7, 'c': 8, 'd': 6, 'e': 1}
result = filter_even_values(my_dict)
print(result)  # Output: {'b': 2, 'd': 4}
