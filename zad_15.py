def diff(x):
    def diff_inner(y):
        return x - y
    return diff_inner

# Przykłady użycia:
diff_five = diff(5)
print(diff_five(3))  # Output: 8
print(diff(2)(3)) 