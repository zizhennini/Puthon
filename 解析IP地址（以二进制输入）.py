def validate_binary(binary_str, length=32):
    """
    验证输入的二进制字符串是否符合要求（长度等）
    """
    if len(binary_str)!= length:
        raise ValueError(f"输入的二进制字符串长度必须为 {length} 位")
    if not all(char in "01" for char in binary_str):
        raise ValueError("输入的字符串必须只包含0和1")
    return binary_str


def calculate_network_host(binary_ip, binary_mask):
    """
    根据二进制格式的IP地址和子网掩码计算网络号和主机号
    """
    binary_ip = validate_binary(binary_ip)
    binary_mask = validate_binary(binary_mask)

    network_binary = ""
    host_binary = ""
    for i in range(32):
        # 按位与运算得到网络号的每一位
        network_binary += str(int(binary_ip[i]) & int(binary_mask[i]))
        # 按位异或运算得到主机号的每一位
        host_binary += str(int(binary_ip[i]) ^ int(binary_mask[i]))

    return network_binary, host_binary


# 示例用法
binary_ip = "11000000101010000000000101100100"
binary_mask = "11111111111111111111111100000000"

network_result, host_result = calculate_network_host(binary_ip, binary_mask)
print(f"网络号（二进制）: {network_result}")
print(f"主机号（二进制）: {host_result}")

# 可以添加转换函数将二进制结果转换为十进制点分格式展示（参考之前提供的代码中的转换函数）
# 例如：
def binary_to_ip(binary_ip):
    """将二进制格式的IP地址转换为十进制点分格式"""
    if len(binary_ip)!= 32:
        raise ValueError("输入的二进制IP地址长度必须为32位")
    octets = [binary_ip[i:i + 8] for i in range(0, 32, 8)]
    ip_address = []
    for octet in octets:
        decimal_value = int(octet, 2)
        ip_address.append(str(decimal_value))
    return '.'.join(ip_address)

print(f"网络号（十进制点分格式）: {binary_to_ip(network_result)}")
print(f"主机号（十进制点分格式）: {binary_to_ip(host_result)}")