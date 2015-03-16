# Finding the maximum value

datalist = [18, 3, 7, -32, 123, 42, 7, 123, -9]

def max1(data):
    """Return maximum value in data"""
    maxval = float('-inf')
    for item in data:
        if item > maxval:
            maxval = item
    return maxval

print max1(datalist)

def max2(data):
    """Return maximum value in data"""
    return max(data)

print max2(datalist)

def max3(data):
    """Return index and value of maximum value in data"""
    maxval = float('-inf')
    maxidx = None
    for idx in range(len(data)):
        if data[idx] > maxval:
            maxval = data[idx]
            maxidx = idx
    return maxidx, maxval

print max3(datalist)

def max4(data):
    """Return index and value of maximum value in data"""
    maxval = max(data)
    maxidx = data.index(maxval)
    return maxidx, maxval

print max4(datalist)

def max5(data):
    """Return list of maximum values in data"""
    maxvals = []
    for item in data:
        if (len(maxvals) == 0):
            maxvals.append(item)
        elif item == maxvals[0]:
            maxvals.append(item)
        elif item > maxvals[0]:
            maxvals = [item]
    return maxvals

print max5(datalist)

def max6(data):
    """
    Return list of index and value of
    maximum values in data
    """
    maxvals = []
    for idx in range(len(data)):
        item = data[idx]
        if (len(maxvals) == 0):
            maxvals.append((idx, item))
        elif item == maxvals[0][1]:
            maxvals.append((idx, item))
        elif item > maxvals[0][1]:
            maxvals = [(idx, item)]
    return maxvals

print max6(datalist)
