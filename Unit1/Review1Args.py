#复习一下函数的参数

#位置参数
def power(x):
    return  x*x
#print(power(222))

#默认参数
def power(x,n=2):
    result =1
    while True :
        result = result * x
        n = n - 1
        if(n<1):
         return result ;
print(power(9,1))

def power(x, n=2):
    s =1
    while n>0:
        s*=x
        n-=1
    return  s
print(power(9,2))

#可变参数
from  functools import  reduce

def cacl(*numbers):
    return  reduce(lambda x,y:x +y,numbers)
print(cacl(9,2,12,334))


#关键字参数

def person(name ,age ,**kw):
    return  "name:"+name+" age:"+age+" kw:"+str(kw) ;
print(person("szhua","20"))
print(person("szhua","90",leilei="myWIfe"))


#命名关键字参数

def perspm(name,age,*,city,married):
    print(name,age,city,married)

perspm("szhua",20,city="liaocheng",married=True)


#命名关键字和可变参数之间

def person (name ,age ,*args ,city ,married):
    print(name,age,args,city,married)
person("szhua",111,999,9999,city="jiNan",married=True)

#所有的方法参数都可以写成这样

def person(*args,**kwargs):
    print(args,kwargs)

person("sz","fsdf","ffff",ke=True,married =True)


import  time

def log(func):
    def wrrapper(*args,**kwargs):
      print("method %s() called"%func.__name__)
      return func(*args,**kwargs)
    return wrrapper

# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

#@log 相当于执行了 now =log(now)==> return wrrapeer  即 now =wrrapper 换了方法;
@log
def now():
    print(time.time())
#will print wrapper !!

import  functools
def log(text):
    def decorator(func):
       #调换名称！！
       @functools.wraps(func)
       def wrraper(*args,**kwargs):
            print("%s:method %s() called" % (text,func.__name__))
            return func(*args,**kwargs)
       return  wrraper
    return  decorator

@log("szhua")
def now():
    print(time.time())
now()



from functools import wraps
from time import time, sleep

start_time = time()
print("\n现在开始运行...\n\n**********************\n")

def log(text):
    def decorator(func):
        @wraps(func)
        def wrapers(*args, **kw):
            print("函数{0}()即将执行，此时系统已运行了 {1} 秒\n".format(func.__name__, time()-start_time))
            startTime =  time()
            return (func(*args, **kw),print("函数{0}()执行了 {1} 秒后，结束了自己\n".format(func.__name__, time()-startTime)))[0]
        return wrapers
    #这句话：若是和text.str和text相同，即是个字符串的时候那么就是log('txt') 否则是传递的函数名称)
    return (decorator,print("我是一个带参数的装饰器，我的参数是 '{}' ".format(text) ))[0] if text.__str__() == text else decorator(text)

@log
def abc():
   # print("我是函数abc(),我正在执行中，不过我要睡 5 秒\n")
    sleep(5)

# @log('嘿，伙计，是你吗？\n')
# def efg():
#     #print("我是函数efg(),我正在执行中，我只想睡 3 秒\n")
#     sleep(3)

abc()
#efg()

print("运行结束，一共运行了",time()-start_time,"秒")


def ioiio():
    return ""
print(ioiio.__str__())





























