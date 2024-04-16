def map_nested(func, nested_list):
    return [map_nested(func, sublist) if isinstance(sublist, list) else func(sublist) for sublist in nested_list]


def square(x):
    return x ** 2

nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, [9, 10]]]
result = map_nested(square, nested_list)
print(result) 
