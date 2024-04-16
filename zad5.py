def generate_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci_gen = generate_fibonacci()
for i in range(10): 
    print(next(fibonacci_gen))
