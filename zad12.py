def rotate_list(input_list, steps):
    if not input_list:
        return input_list
    steps = steps % len(input_list)
    return input_list[-steps:] + input_list[:-steps]

my_list = [0, 9, 3, 6, 6, 5, 6, 4, 2, 1]
rotated_list = rotate_list(my_list, 2)
print(rotated_list) 
