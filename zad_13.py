def calculate_factorial(x):
    if x > 1:
        return x*calculate_factorial(x-1)
    return 1

print(calculate_factorial(6))
