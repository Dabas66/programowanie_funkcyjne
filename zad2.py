from itertools import combinations

def combinations_generator(elements):
    all_combinations=list(combinations(elements,2))
    return all_combinations

print(combinations_generator(['a','v','h','b']))