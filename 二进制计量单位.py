def unit_convert(a):
    if 1 <= a < 1024:
        b = a
    elif 1024 <= a < 1024 ** 2:
        b = round(a / 1024, 1)
    elif 1024 ** 2 <= a < 1024 ** 3:
        b = round(a / (1024 ** 2), 1)
    elif 1024 ** 3 <= a < 1024 ** 4:
        b = round(a / (1024 ** 3), 1)
    elif 1024 ** 4 <= a < 1024 ** 5:
        b = round(a / (1024 ** 4), 1)
    return b


a = 1024
b = unit_convert(a)
print('%s -> %s' % (a, b))
