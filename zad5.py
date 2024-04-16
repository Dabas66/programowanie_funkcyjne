is_palindrome = lambda s: ''.join(filter(str.isalnum, s.lower())) == ''.join(filter(str.isalnum, s.lower()))[::-1]

print(is_palindrome('kamilślimak'))
print(is_palindrome('policja'))





