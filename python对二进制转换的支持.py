bin_num = input("请输入一个二进制数：")
decimal_num = int(bin_num, 2)
octal_num = oct(decimal_num).lstrip("0o")
print(f"对应的八进制数是：{octal_num}")