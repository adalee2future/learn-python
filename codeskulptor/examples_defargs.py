"""
Simple program to illustrate how default arguments
are handled.
"""

def mystery(item, sequence=[1, 2, 3]):
    """
    Function with unintuitive behavior.
    """
    sequence.append(item)
    return sequence

print mystery(4)
print mystery(5)
