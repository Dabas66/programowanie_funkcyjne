def square(x):
    return x ** 2

numbers = [6,4,7,99]
squared_numbers = list(map(square,numbers))
print(squared_numbers)