def binary_to_ip(binary_ip):
    # 确保传入的二进制字符串长度为32位
    if len(binary_ip)!= 32:
        raise ValueError("输入的二进制IP地址长度必须为32位")
    # 按8位一组进行分割
    octets = [binary_ip[i:i + 8] for i in range(0, 32, 8)]
    ip_address = []
    for octet in octets:
        # 将每8位二进制转换为十进制
        decimal_value = int(octet, 2)
        ip_address.append(str(decimal_value))
    return '.'.join(ip_address)

# 示例用法
binary_ip = "11000000101010000000000100000001"
print(binary_to_ip(binary_ip))