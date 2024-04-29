from itertools import permutations

def generate_permutations(input_list):
    return list(permutations(input_list))

my_list = [ 1, 10, 100]
result = generate_permutations(my_list)
print(result)
