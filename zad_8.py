from functools import reduce

numbers = [6,4,7,322,34]

sum_numbers = reduce(lambda a,b:a+b,numbers)
print(sum_numbers)