for i in range(1, 10):
    for j in range(1, i + 1):
        # 修改了print语句中的格式化方式
        print(f"{j} x {i}={i * j}\t", end=" ")
    print("")
