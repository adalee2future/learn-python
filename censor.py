def censor(text, word):
    res = ""
    text = text.split()
    n = len(text)
    m = len(word)
    for i in range( n - 1):
        if text[i] == word:
            res += ("*" * m + " ")
        else:
            res += (text[i] + " ")
    if text[n-1] == word:
        res += ("*" * m)
    else:
        res += text[n-1]
    return res