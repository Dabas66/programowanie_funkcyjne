from itertools import groupby

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(num):
    return num % 2 == 0

grouped_numbers = groupby(numbers, key=is_even)
odd_list=[]
even_list=[]
for key, group in grouped_numbers:
    if key:
        even_list.append(list(group)[0])
    else:
        odd_list.append(list(group)[0])
print(f'Even numbers: {even_list}')
print(f'Odd numbers: {odd_list}')