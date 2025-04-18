for i in range(1,10):                   # 打印的行数
    for j in range(1,i+1):              # 打印的列数
        print(j,'*',i,'=',f'{i*j:<4}',end='')
    print()