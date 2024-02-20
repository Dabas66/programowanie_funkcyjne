def even(numbers):
    even_numbers = []
    for number in numbers:
        if number%2==0:
            even_numbers.append(number)
    return even_numbers

field = lambda a,b: a*b

