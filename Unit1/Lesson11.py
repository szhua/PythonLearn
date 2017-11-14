#map reduce
def add(x):
    return  x+10+x*11

x =map(add,list(range(10)))
print(list(x))

from functools import  reduce

def add(x,y=0):
    return x+10+x*11
y =reduce(add,map(add,list(range(10))))
print(y)

def char2num(s):
    return  {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[s]

def getResult(x,y):
    return  x*10+y

#str to int
print(reduce(getResult,map(char2num,"111114343")))
#str to int
print(int("111114343"))
print(list(map(char2num,"10")))

def str2int(s):
    return  reduce(lambda x,y:x * 10+y,map(char2num,s))
print(str2int("90904930"))

def normalize(s):
    return  s[0].upper()+(s[1:len(s)]).lower()
print(list(map(normalize,['adam', 'LISA', 'barT'])))

#求积
def prod(L):
    return reduce(lambda x,y:x*y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
print(3 * 5 * 7 * 9)
print("3333.444".index("."))


#char 转换成 num
def char2num(s):
    return  {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[s]
#int 转换成num
def int2flot(s,o):
    return s/10**o
#string 转换成 int
def str2int(s):
    return  reduce(lambda x,y:x*10+y,map(char2num,s)) ;
def str2float(s):
    s =str(s)
    before=str2int(s[:s.index(".")])
    after =str2int(s[s.index(".")+1:])
    after =int2flot(after,len(s[s.index(".")+1:]))
    return  before+after

print(str2float("999.11"))
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(lambda name: name.capitalize(), L1))
print(L2)
print("IoIoIo".capitalize())
print(10**4)

'''
filter函数
Python内建的filter()函数用于过滤序列。
'''
def isOdd(s):
    return  s%2 == 0
print(list(filter(isOdd,[1,2,3,4,5,6,67,7,8,9])))

def notEmpty(s):
    return  s and s.strip()
print(list(filter(notEmpty,["ff",None," "])))

'''
可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
'''
def createInter():
    n =1
    while True:
     yield  n
     n+=2
     if(n==101):
         break
#print(list(createInter()))

def _not_divisible(n):
    return lambda x: x % n > 0
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def getResult():
    yield 2
    t =createInter()
    while True:
       n = next(t)
       yield n
       t =filter(_not_divisible(n),t)

def primes():
   yield 2
   it = _odd_iter()  # 初始序列
   while True:
       n = next(it)  # 返回序列的第一个数
       yield n
       it = filter(_not_divisible(n), it)  # 构造新序列

it =primes()
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
