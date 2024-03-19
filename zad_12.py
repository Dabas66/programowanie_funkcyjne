from functools import partial

def multiply(x,y):
    return x * y

triple = parital(multiply,3)

print(triple(10))
