

#Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。


import  itertools

#从10开始数自然数
naturals =itertools.count(10)
from collections import  Iterator

#判断naturals的类型
print(isinstance(naturals,Iterator))

for x in naturals:
    if x>70:
        break
    print(x)

#cycle()会把传入的一个序列无限重复下去：
cycles =itertools.cycle("szhualeilei")
print(isinstance(cycles,Iterator))
n =0
for x in cycles :
    #print(x)
    n+=1
    if n >100:
        break

#repeat 重复
repeats =itertools.repeat("szhua",10)
for x in repeats:
    print(x)

inter =(x**2 for x in range(100) if x%2==0and x%3==0)

#使用take while对Iterrator进行过滤：
ns =itertools.takewhile(lambda x :x<1000,inter)
print(list(ns))

#chain()
#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
print(list(itertools.chain("fjksjdfk","abcdefghijklmn")))

#groupby()
#groupby()把迭代器中相邻的重复元素挑出来放在一起：

for key ,value in itertools.groupby("aaajjjfdsfkkkfffff"):
    print(str(key).upper(),list(value))















