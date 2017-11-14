

#切片

L=["szhua","leilei","safr"]
#从零索引开始往后输出2个
print(L[0:2])
#输出倒数两个开始的
print(L[-2:])

L =list(range(1000))
print(L[:989:2])
print(L[:-10:2])
#打印所有的数
print(L[:])
print(L[::2])

#迭代
kv ={"szhua":1,"leilei":"boss"}
for values in kv:
    print(values)

for values in kv.items():
    print(values)

for k,v in kv.items():
    print(k,":",v)

from collections import Iterable
#检查是否可以进行迭代
print(isinstance(kv ,Iterable))


for i,values in enumerate (["szhua","leilei"]):
     print(i,":",values)

















