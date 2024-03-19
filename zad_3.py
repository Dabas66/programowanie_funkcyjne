def filter_even_numbers(numbers):
    filtered_numbers = []
    for number in numbers:
        if number%2==0:
            filtered_numbers.append(number)
    return filtered_numbers

print(filter_even_numbers([1,2,3,4,5,6,7,8,9]))