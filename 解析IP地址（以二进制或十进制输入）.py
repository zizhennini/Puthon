def ip_to_binary(ip_address):
    """将十进制点分格式的IP地址转换为二进制格式"""
    octets = ip_address.split('.')
    binary_ip = ""
    for octet in octets:
        decimal_value = int(octet)
        binary_octet = bin(decimal_value)[2:].zfill(8)
        binary_ip += binary_octet
    return binary_ip


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


def calculate_network_host(ip, subnet_mask):
    """
    根据IP地址和子网掩码计算网络号和主机号
    """
    # 先统一转换为二进制
    binary_ip = ip_to_binary(ip) if '.' in ip else ip
    binary_mask = ip_to_binary(subnet_mask) if '.' in subnet_mask else subnet_mask

    network_binary = ""
    host_binary = ""
    for i in range(32):
        network_binary += str(int(binary_ip[i]) & int(binary_mask[i]))
        host_binary += str(int(binary_ip[i]) ^ int(binary_mask[i]))

    network_ip = binary_to_ip(network_binary)
    host_ip = binary_to_ip(host_binary)
    return network_ip, host_ip


# 示例用法（以十进制点分格式输入）
ip = "192.168.1.100"
subnet_mask = "255.255.255.0"
network, host = calculate_network_host(ip, subnet_mask)
print(f"网络号: {network}")
print(f"主机号: {host}")

# 示例用法（以二进制格式输入）
ip_binary = "11000000101010000000000101100100"
subnet_mask_binary = "11111111111111111111111100000000"
network_binary_result, host_binary_result = calculate_network_host(ip_binary, subnet_mask_binary)
print(f"网络号（二进制）: {network_binary_result}")
print(f"主机号（二进制）: {host_binary_result}")