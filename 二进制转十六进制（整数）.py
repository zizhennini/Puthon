def BinToHex_int(b):
    hex_b = "0123456789ABCDEF"
    result = []
    b = str(b)  # 将传入的参数转换为字符串类型，确保后续操作正确
    while len(b) % 4!= 0:
        b = "0" + b
    for i in range(0, len(b), 4):
        group = b[i:i + 4]
        decimal_val = 0
        for j in range(4):
            decimal_val += int(group[j]) * 2 ** (3 - j)  # 修正此处，先转换为整数再进行计算
        hex_val = hex_b[decimal_val]
        result.append(hex_val)
    return "".join(result)

b = "10101101"  # 将参数修改为字符串类型
h = BinToHex_int(b)
print('%s -> %s' % (b, h))