def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

nested_list = [12, [23, 37], [45, [8, 87]], 54, [4, [90, 10]]]
result = flatten_list(nested_list)
print(result)