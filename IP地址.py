def parseIP(ip, mask):
    # 将IP地址和子网掩码按点分割成字符串列表
    ip_octets = ip.split('.')
    mask_octets = mask.split('.')

    network_octets = []
    host_octets = []

    for i in range(4):
        # 将每一段的字符串转换为整数，方便后续进行位运算
        ip_num = int(ip_octets[i])
        mask_num = int(mask_octets[i])

        # 计算网络号的每一段，通过按位与运算（&）
        network_octet = ip_num & mask_num
        network_octets.append(network_octet)

        # 计算主机号的每一段，正确做法是先取反子网掩码，再与IP地址按位
        host_octet = ip_num & (~mask_num)
        host_octets.append(host_octet)

    # 将网络号和主机号的每一段列表转换为十进制点分格式的字符串
    network = '.'.join(map(str, network_octets))
    host = '.'.join(map(str, host_octets))

    return network, host


# 使用字符串表示的IP地址和子网掩码
ip = "168.16.127.253"
mask = "255.255.192.0"

# 计算网络号和主机号（十进制点分格式）
netID, hostID = parseIP(ip, mask)

print('网络号：', netID)
print('主机号：', hostID)
