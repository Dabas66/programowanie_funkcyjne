def odd_numbers():
    num = 1
    while True:
        yield num
        num += 2
odd_gen=odd_numbers()

for x in range(5):
    print(next(odd_gen))
