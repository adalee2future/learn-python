def check_bit4(input_num):
    mask = 0b1000
    desired = input_num & mask
    if desired > 0:
        return "on"
    else:
        return "off"
       
print check_bit4(0b1111111111111)
print check_bit4(0b10101010)
print check_bit4(0b1011100011)