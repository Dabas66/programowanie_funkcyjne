def recursive_sum(nested_list):
    total_sum = 0
    for element in nested_list:
        if isinstance(element, list):
            total_sum += recursive_sum(element)
        else:
            total_sum += element
    return total_sum

nested_list = [8,[3, 43,56, [55, 64,55]], 30, [63, [88, 10]]]
result = recursive_sum(nested_list)
print(result)
