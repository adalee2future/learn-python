m = ['have', 'fun']
x, y = m
print x
print y


(a, b) = m
print a
print b

a, b = b, a
print a
print b

addr = 'monty@python.org'
uname, domain = addr.split('@')
print uname
print domain