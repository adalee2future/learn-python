def is_prime(x):
    if x <= 1:
        return False
    for n in range(2, x):
        if x % n == 0:
            return False
    return True
    
print is_prime(2)
print is_prime(3)
print is_prime(4)
print is_prime(5)
print is_prime(6)