


#collections是Python内建的一个集合模块，提供了许多有用的集合类。

#namedtuple
from collections import  namedtuple

#创建一个Point的class
#@params point 类名 x,y
Point =namedtuple("Point",["x","y"])

point =Point(1,2)
print(point)

print(isinstance(point,Point))
#True
print(isinstance(point,tuple))
#True

"使用list存储数据时，按索引访问元素很快" \
"，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。"

#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈

from collections import  deque

q =deque()
q.append("a")
q.append("n")
#左边的插入
q.appendleft("s")
print(q)
#直接从左边进行删除
q.popleft()
print(q)

"使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict:"
from collections import  defaultdict

ddict =defaultdict(lambda :"None")
ddict["aa"] ="leilei"
print(ddict["aa"])
#====leilei
print(ddict["bb"])
#===None

"""使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。

如果要保持Key的顺序，可以用OrderedDict："""
#OrderedDict
from collections import  OrderedDict

d =dict([('o', 1), ('b', 2), ('c', 3)])
#有时候会变成无序的，确保他的有序情况下
print(d)

od=OrderedDict([('o', 1), ('b', 2), ('c', 3)])

print(od)



#Counter
#Counter是一个简单的计数器，例如，统计字符出现的个数：

from collections import  Counter

c =Counter()

for x in "woshizhendeainileilei":
    c[x]+=1

def order(x):
    return x[1]

L =list(c.items())
print(L)
print(sorted(L,key=lambda x :x[1]))
print(sorted(["a","w","n"],key=str.lower))


"""collections是Python内建的一个集合模块，提供了许多有用的集合类
namedtuple:
    namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
deque：
    deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈。可以再首或者尾进行删除和插入
defaultdict:
    使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
OrderedDict
    可以保证key的顺序"""