def remove_duplicates(array):
    res = []
    for a in array:
        is_a_in_res = False
        for r in res:
            if a == r:
                is_a_in_res = True
                break
        if not (is_a_in_res):
            res.append(a)
    return res
    
print remove_duplicates([1,2,3,4,3,2,6,7,7,8,5])
