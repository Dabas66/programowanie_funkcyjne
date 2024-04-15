numbers = [3, 12, 5, 8, 15, 7]
squared_greater_than_10 = [square for num in numbers if (square := num ** 2) > 10]
print(squared_greater_than_10)