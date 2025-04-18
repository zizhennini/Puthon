firstASCII = 0  # 改为0，使其能涵盖更广泛范围从0开始的字符编码
N = 65536  # 支持的字符总数改为65536，对应较广泛的Unicode编码范围常用部分

def enChar(x, key):
    xid = ord(x) - firstASCII
    yid = (xid + key) % N
    y = chr(firstASCII + yid)
    return y


def Caesar(text, key):
    result = ''
    for x in text:
        code = ord(x)
        if 0 <= code <= 65535:  # 判断字符编码是否在设定的范围内，以此决定是否加密
            x = enChar(x, key)
        result = result + x
    return result


key = 2  # 密钥
text = input()
enText = Caesar(text, key)
print('%s -> %s' % (text, enText))