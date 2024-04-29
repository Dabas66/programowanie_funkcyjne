def remove_whitespace(string_list):
    return [string.strip() for string in string_list]

string_list = ["  jbc  ", "rofl  ", "lol     ", "    xddddd   "]
result = remove_whitespace(string_list)
print(result)
