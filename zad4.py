def power_function(exponent):
    return lambda x: x ** exponent

square = power_function(2)
cube = power_function(3)

print(square(3))  
print(cube(3))
