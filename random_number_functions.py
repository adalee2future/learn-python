import random

# choice
name = 'Ada Lee'
ll = [1, 2, 3, 4, 5]
tt = (6, 7, 8, 9)

print random.choice(name)
print random.choice(ll)
print random.choice(tt)

# randrange
print random.randrange(100, 1000, 2)
print random.randrange(100, 1000, 3)

# random
for i in range(5):
    print random.random()
    
# seed
for i in range(10):
    random.seed(456)
    print random.random()
    
# shuffle
random.shuffle(ll)
print ll

# uniform
# The method uniform() returns a random float r,
# such that x is less than or equal to r and r is less than y.
for i in range(5):
    print random.uniform(5, 10)