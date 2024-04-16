def filter_long_words(word_list):
    avg_length = sum(len(word) for word in word_list) / len(word_list)
    return [word for word in word_list if len(word) > avg_length]

words = ['police','port','log','mountain']
filtered_words = filter_long_words(words)
print(filtered_words)
