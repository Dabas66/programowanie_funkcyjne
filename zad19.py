def check_anagrams(string1, string2):
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")
    
    if len(string1) != len(string2):
        return False
    
    return sorted(string1) == sorted(string2)

string1 = "listen"
string2 = "silent"
result = check_anagrams(string1, string2)
print(result) 