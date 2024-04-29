def apply_function_to_tuples(tuple_list, func):
    return [func(*t) for t in tuple_list]

def sum_tuple(a, b):
    return a + b

tuple_list = [(6, 2), (7, 8), (10, 1)]
result = apply_function_to_tuples(tuple_list, sum_tuple)
print(result)
