def capitalize_all_words(input_string):
    return ' '.join(word.capitalize() for word in input_string.split())


input_string = "see you later aligator"
result = capitalize_all_words(input_string)
print(result)
