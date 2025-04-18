def decimal_to_binary(num):
    #整数部分吧
    integer_part = int(num)
    binary_integer_part = bin(integer_part)[2:] if integer_part else '0'

    #小数部分
    decimal_part = num - integer_part
    binary_decimal_part = ''
    while decimal_part and len(binary_decimal_part) < 10:
        decimal_part *=2
        binary_decimal_part += str(int(decimal_part))
        decimal_part -=int(decimal_part)

    return binary_integer_part + ('.' + binary_decimal_part if binary_decimal_part else '')
b = 123
d = decimal_to_binary(b)
print('%s -> %s' % (b,d))




