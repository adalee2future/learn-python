def median(array):
    n = len(array)
    array = sorted(array)
    if n % 2 == 0:
        print "here"
        return float(array[n/2] + array[n/2 - 1]) / 2
    else:
        return array[n/2]
        
array = [4,5,5,4]

print median(array)
        
