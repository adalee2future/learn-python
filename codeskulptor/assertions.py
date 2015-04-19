"""
Using assertions.
"""

import math

def hypotenuse(sidea, sideb):
    """
    Calculate the length of hte hypotenuse of a right
    triangle with sides of length sidea and sideb
    """
    # Compute hypotenuse
    hyp = math.sqrt(sidea + sideb)

    # Make sure value is reasonable
    assert hyp > sidea and hyp > sideb, "hypotenuse too short"
    assert hyp < (sidea + sideb), "hypetenuse too long"

    return hyp

#print hypotenuse(3, 4)

def odd_fraction(lst):
    """
    Return the fraction of add lements in lst
    """
    odds = 0
    total = 0

    # Count odd numbers
    for item in lst:
        if item % 2:
            odds += 1
        total += 1

    # Make sure we don't divide by 0
    assert total != 0, "no elments"
    assert total <= total, "too many odds!"

    fraction = float(odds) / total
    return fraction

numbers = [2, 8, 1, 4, 3, 7, 9]
print odd_fraction(numbers)
