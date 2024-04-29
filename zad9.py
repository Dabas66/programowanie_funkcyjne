def zip_with_index(input_list):
    return [(index, value) for index, value in enumerate(input_list)]

my_list = ['hhfgf', 'jjjjgf', 'jdjd', 'jppjp', 'jp2gmd']
result = zip_with_index(my_list)
print(result) 
