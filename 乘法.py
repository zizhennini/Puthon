m,n = map(int,input().split())

for i in range(1,n//2):
    print(' '* (i-1) + '*' * m + ' '*(2*m+1-2*i) + '*' * m)


for j in range(1,n-n//2):
    print(' ' * (n-n//2 - 1) + '*' * m + ' ' * (n-n//2 - 1) + '*' * m)