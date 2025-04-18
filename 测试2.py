firstASCII = 32  # 可视字符范围起始ASCII码，这里以空格开始作为首个可视字符的ASCII码
N = 95  # 可视ASCII字符的总数（126 - 32 + 1 = 95）


def enChar(x, key):
    xid = ord(x) - firstASCII
    yid = (xid + key) % N
    y = chr(firstASCII + yid)
    return y


def Caesar(text, key):
    result = ''
    for x in text:
        ascii_code = ord(x)
        if 32 <= ascii_code <= 126:  # 判断是否是可视ASCII字符范围
            x = enChar(x, key)
        result = result + x
    return result


key = 2  # 密钥
text = input()
enText = Caesar(text, key)
print('%s -> %s' % (text, enText))
