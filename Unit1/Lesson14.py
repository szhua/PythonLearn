
#Lesson14 修饰函数:闭包的应用
def log(text):
    def decorator(func):
         def wrraper(*args,**kwargs):
             if(isinstance(text,str)):
              print('%s: call %s()' % (text, func.__name__))
             else:
               print('call %s()'%text.__name__)
             return func(*args,*kwargs)
         return wrraper
    return  decorator  if(isinstance(text,str)) else decorator(text)
@log
def name():
    return None
name()
"""
resolved!!
"""

import  functools

#修改关键字函数；命名关键字函数参数
int2 =functools.partial(int ,base=2)
int2('100100')
print(int2("100000"))






















