nums = [3, 41, 12, 9, 74, 15]

largest = None
for itervar in nums:
    if largest is None or itervar > largest :
        largest = itervar
    print 'Loop: ', itervar, largest
print 'largest: ', largest

smallest = None
for itervar in nums:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print 'Loop: ', itervar, smallest
print 'smallest: ', smallest

