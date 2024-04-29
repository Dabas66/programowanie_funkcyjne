def partition_list(input_list, condition):
    true_list = [item for item in input_list if condition(item)]
    false_list = [item for item in input_list if not condition(item)]
    return true_list, false_list

def is_even(x):
    return x % 2 == 0

my_list = [78,88,89,55,33,4,6,1,32,4,5]
true_part, false_part = partition_list(my_list, is_even)
print("True elements:", true_part)
print("False elements:", false_part)
