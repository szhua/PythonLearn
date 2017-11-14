

#生成器 generate


#
# classmates =['ff',"szhua","leilei"]
# L=[x+x for x in classmates ]
#
# print(L)
#
# g =(x for x in classmates)
#
# print(g)
#
# for x in L:
#     print(x)
#
# #斐波拉契数列
# def fib(max):
#     n,a,b =0 ,0 ,1
#     while n<max:
#         yield b
#         #a=>b b=>a+b  一直往前赶着走
#         a,b =b,a+b
#         n+=1 ;
# for x in fib(10):
#     print(x)
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)
#     return "done"
#
# for x in odd():
#     print(x)
#
# o =odd()
# while True:
#     try:
#         print(next(o))
#         #此处捕获返回值
#     except StopIteration as e:
#         print(e.value)
#         break
#
# #
# #1
# #1   1
# #1   2   1
# #1   3   3   1
# # 1   4   6   4   1
# #1   5   10  10  5   1
# #
#
# def triangles():
#     L=[1];
#     while True :
#         yield  L
#         L=[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]
# n=0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 2:
#         break

###range [0,len-1) 左闭右开
##range（len-1）: 则 循环到len-2  则：L(len-2+1)为最后的一个

def trangles():
    L =[1]
    while True:
     yield L
     L=[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]
n=0

for t in trangles():
    print(t)
    n =n+1
    if n==90:
        break





























