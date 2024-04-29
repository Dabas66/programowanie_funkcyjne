def custom_sort(input_list, key_func):
    return sorted(input_list, key=key_func)


my_list = [100,67,90,22,3,1,4]
sorted_list = custom_sort(my_list, lambda x: -x) 
print(sorted_list)
