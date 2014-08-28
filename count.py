def count(sequence, item):
    res = 0
    for i in sequence:
        if i == item:
            res += 1
    return res