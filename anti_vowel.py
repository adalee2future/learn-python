def anti_vowel(text):
    res = ""
    for c in text:
        if c == 'A' or c == 'O' or c =='E' or c =='I' or c == 'U' or c == 'a' or c == 'o' or c == 'e' or c == 'i' or c == 'u':
            continue
        res += c
    return res
    
print anti_vowel("Hey, man, how are you these days?")
    