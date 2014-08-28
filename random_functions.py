import random

for i in range(10):
    x = random.random()
    print x
    
print random.randint(5, 10)

names = ['Bob', 'Ada', 'Lucy', 'Mike']
lucy_name = random.choice(names)
print lucy_name
