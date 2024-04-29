def cumulative_sum(input_list):
    cumulative_sum_list = []
    running_sum = 0
    for item in input_list:
        running_sum += item
        cumulative_sum_list.append(running_sum)
    return cumulative_sum_list


my_list = [10,10,20,30,50]
result = cumulative_sum(my_list)
print(result) 
