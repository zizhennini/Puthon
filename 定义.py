#def test(b = 2,a = 4):
    #global z
    #z = a * b
    #return z
#z =10
#print(z,test())
# def Sum(a,b,c=5):
#     b=3
#     print(a,b,c)
# Sum(a=8,c=2)
# for s in "testatest":
#     if s =="a" or s =="e":
#         continue
#     print(s,end='')
# text = "hello word"
# print(text.title())
# def Sum(*p):
#     return sum(p)
# print(Sum(3,5,8))
# for i in range(1,6):
#     if i%4==0:
#         break
#     else:
#         print(i,end=",")
#
# a=[1,2,3,None,[[]],[]]
# print(len(a))
# def func(num):
#     num *=2
# x =20
# func(x)
# print(x)
# x = 0
# for i in range(5):
#     x +=1
#     if i % 2==0:
#         continue
#     x +=1
# print(x)
# a,b,c,d =1,3,5,4
# if a<b:
#     if c<d:
#         x=1
#     elif a<c:
#         if b<d:
#             x=2
#         else:
#             x=3
#     else:
#         x=6
# else:
#     x=7
# print(x)
n = int(input())
m = 0
for i in range(n):
    if i % 37 == 0:
        m += i
    print(m)
    if i % 37 != 0:
        print("0")