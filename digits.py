def is_ordered(ls):
    '''
    check whether list ls is in ascending order or descending order
    '''
    tmp = ls[:]
    tmp.sort()
    if ls == tmp:
        return True
    tmp.reverse()
    if ls == tmp:
        return True
    return False
    
def num2list(num):
    ''' 
    convert a number ranging from 0 to 99999 to a list of 5 elements
    i.e., 0 -> [0, 0, 0, 0, 0], 123 -> [0, 0, 1, 2, 3], 34506 -> [3, 4, 5, 0, 6]
    '''
    ss = str(num)
    while len(ss) < 5:
        ss = '0' + ss
    return list(ss)

# rate of asecending or descending with repetition allowed
total = 100000.0
count = 0
for num in range(100000):
    if is_ordered(num2list(num)):
        count += 1
print count, count / total 


# rate of asecending or descending with repetition not allowed
total = 0.0
count = 0
for num in range(100000):
    numlist = num2list(num)
    if len(numlist) == len(set(numlist)):
        total += 1
        if is_ordered(num2list(num)):
            count += 1
print count, total, count / total
