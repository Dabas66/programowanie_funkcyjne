def remove_duplicates(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

input_list = [2,1,1,3,1,2,2,7,7,1,2,3]
result = remove_duplicates(input_list)
print(result)
