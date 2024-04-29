def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def read_large_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line

fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))

file_gen = read_large_file('large_file.txt')
for line in file_gen:
    print(line)
