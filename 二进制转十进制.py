def BinToDec(b):
    # 确保b是一个字符串，以便可以使用.startswith等字符串方法
    b = str(b)

    # 检查是否为负数
    if b.startswith('-'):
        is_negative = True
        b = b[1:]
    else:
        is_negative = False

    # 分离整数部分和小数部分
    if '.' in b:
        int_part, frac_part = b.split('.')
    else:
        int_part = b
        frac_part = ''

    # 计算整数部分的十进制值
    int_val = sum(int(digit) * (2 ** i) for i, digit in enumerate(reversed(int_part)))

    # 计算小数部分的十进制值
    frac_val = sum(int(digit) * (2 ** (-i - 1)) for i, digit in enumerate(frac_part))

    # 结果考虑正负
    result = int_val + frac_val
    if is_negative:
        result = -result

    return result

b = 1101.01
#b = input("字符串形式给出的二进制数")  # 确保b是以字符串形式给出的二进制数
p = BinToDec(b)
print('%s -> %s' % (b, p))
