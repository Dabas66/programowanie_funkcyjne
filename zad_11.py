def sort_strings_by_length(strings):
    sorted_strings = sorted(strings, key=lambda x: len(x))
    return sorted_strings

strings = ["banana", "apple", "kiwi", "orange", "grapefruit"]
sorted_strings = sort_strings_by_length(strings)
print(sorted_strings)
