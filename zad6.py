def apply_function_to_list(input_list, func):
    return [func(item) for item in input_list]

def double_value(x):
    return x * 2

my_list = [4, 20, 10, 11, 5]
result = apply_function_to_list(my_list, double_value)
print(result)
