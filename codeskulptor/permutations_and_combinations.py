

import math
print math.factorial(0)


# lottery - 59 balls, draw 6, order is important


print math.factorial(59) / math.factorial(59 - 6)

print math.factorial(59)


num_perms = 1
for idx in range(59, 59 - 6, -1):
    num_perms *= idx
print num_perms

print num_perms / 6
