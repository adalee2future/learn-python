d = {'a': 10, 'b': 1, 'c': 22}

t = d.items()

print t

t.sort() #sort by key

print t

for key, val in t:
    print key, val
    

l = list()

for key, val in d.items():
    l.append((val, key))
    
l.sort(reverse = True) #sort by value
print l