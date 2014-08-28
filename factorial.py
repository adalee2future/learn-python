def factorial(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
    return res
    
print factorial(5)

def rec_fac(x):
    if x == 1 or x == 0:
        return 1
    return x * rec_fac(x - 1)
    
print rec_fac(5)