def compose(f,g):
    def composed_function(x):
        return f(g(x))
    return composed_function

def square(x):
    return x*x

def plus_two(x):
    return x+2


example = compose(square,plus_two)
print(example(2))
        