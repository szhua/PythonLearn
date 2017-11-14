#
# # test function 测试函数；；；；
# #变量指向函数；；；
# a =abs
# print(a(-9000))
# #转换16进制
# print(hex(90909))
#
# n1 = 255
# n2 = 1000
# print(type(hex(666)))
#
# #在此定义函数
# def k(n):
#     print(hex(n))
# k(n1)
# k(n2)
#
# #使用%x表示十六进制
# hex16 = '%x' % (255)
# print(hex16)
# print(hex(255))
#
# def leilei(i):
#     if i>0:
#         return  90
#     else:
#         return  100
# print(leilei(909090))


# def power(x ,n):
#     result =1
#     while n>0:
#         n-=1
#         result*=x
#     return  result


#print(power(10,100))

#默认参数值
def power(x,n=2):
    result =1
    while n>0:
        n-=1
        result*=x
    return  result

print(power(2))


#默认函数
def addpend(a=None):
    if a is None:
        a =[]
    a.append("END")
    print(a)
    return  a ;
addpend()
addpend()
addpend()
addpend()

def cacl(*numbers):
    result =0
    for a in numbers:
        result += a
    return  result

print(cacl(1,2,2,3333,445))
array =[1,2,3,4,5]
#数组调用可变参数
print(cacl(*array))


#关键字参数
def person(name,age,**ss):
    result =print("name",name,"age",age,"othter",ss)
    return result
person("szhua",1111,married=False,wife="leilei")

extras ={"married":False,"wife":"leilei"}
person("szhua",23,**extras)

#命名关键字函数
def test(name,age,*args,city,married):
    print("name:",name,"age",age,"city",city,"married",married,"argS:",args)

test("szhua",90,11,111,111,city="JN",married=extras)

#*args **kw
def index(a,b,c):
    print(a,b,c)
index(*(1,2,23))

#测试一下递归函数
def digui(a):
    if a ==1 :
        return 1
    return a*digui(a-1)
print(digui(100))


#
# def fact(n):
#     return fact_iter(n, 1)
#
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)
#
# fact(1000)

#汉诺塔游戏
def move(n, a, b, c):
    if n == 1:
        print(a,'->',c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
    pass
move(6,'a','b','c')

