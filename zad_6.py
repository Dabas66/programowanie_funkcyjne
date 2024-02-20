def beggin_with_a(word):
        if word[0] == "a":
            return True
        return False
words = ["app","allience","bruh","certain","auto"]

new_words = list(filter(beggin_with_a,words))


def square(number):
    return number ** 2

numbers = [5,7,88,9]

squared_numbers = list(map(square,numbers))

