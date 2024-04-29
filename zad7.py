from collections import defaultdict

def merge_dicts(*dicts):
    merged_dict = defaultdict(int)
    for d in dicts:
        for key, value in d.items():
            merged_dict[key] += value
    return dict(merged_dict)

dict1 = {'a': 2, 'b': 3, 'c': 1}
dict2 = {'b': 3, 'c': 4, 'd': 3}
dict3 = {'c': 8, 'd': 6, 'e': 4}

result = merge_dicts(dict1, dict2, dict3)
print(result)
