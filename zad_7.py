def square(number):
    return number**2
def add_five(number):
    return number+5

def two_func(data):
    data = list(map(square,data))
    data = list(map(add_five,data))
    return data
