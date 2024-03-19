def make_multiplier(x):
    def multiplier(y):
        return x * y
    return multiplier

fun = make_multiplier(4)
print(fun(4))