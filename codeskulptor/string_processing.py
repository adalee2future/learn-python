### String Processing

# String literals
s1 = "Rixner's funny"
s2 = 'Warren wears nice ties!'
s3 = " t-shirits!"
print s1, s2
print s3

# Combining strings
a = ' and '
s4 = "Warren" + a + "Rixner" + ' are nuts!'
print s4

# Characters and slices
print s1[-1]
print len(s1)
print s1[0 : 7] # up to bu not include 7
print s1[0 : 6] + s2[6:]

# Converting strings
s5 = str(375)
print s5[1:]
i1 = int(s5[1:]) + 30
print i1

# Handle single quantity
def convert_units(num, unit):
    result = str(num) + ' ' + unit
    
    if num > 1:
        result += 's'
     
    return result
# convert xx.yy to xx dollars and yy cnets
def convert(val):
    # Split into dillars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))
    
    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")
    
    # Retruen composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string
    
# Tests
print convert(11.23)
print convert(11.20)
print convert(0)