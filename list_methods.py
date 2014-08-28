t = ['c', 'b', 'a', 'g', 'x', 't', 'z', 'y']

t.append('f')
print t

t.extend(['e', 'd'])
print t

t.sort()
print t

t.pop()
print t

t.pop(2)
print t

del t[1]
print t

del t[5:]
print t

t.remove('d')
print t

nums = [3, 41, 12, 9, 74, 15]

print len(nums)
print max(nums)
print min(nums)
print sum(nums)
