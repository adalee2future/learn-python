def purify(list):
    res = []
    for num in list:
        if num % 2 == 0:
            res.append(num)
    return res
    
print purify([1,2,3,4,5,6,7,8,9,10])