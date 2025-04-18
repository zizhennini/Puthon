N = int(input("请输入列表长度N: "))  # 获取列表长度

ls = []

for i in range(N):  # 循环获取N个整数存入列表

        ls.append(int(input("请输入一个正整数: ")))

for num in ls:       # 循环遍历列表

        if  num %5 == 0:

                print(f"列表中第一个5的倍数是: {num}")

                break    # 结束循环