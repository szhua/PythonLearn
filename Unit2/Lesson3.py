#type函数

print(type(123))
print(type("1222222"))




#判断基本类型；
print(type(123)==int)
print(type("str"==str))

def fn():
    return  '"ss'

import  types
#判断其他的类型
#是否是built_in函数
print(type(abs)==types.BuiltinFunctionType)
#是否是lambda
print(type(lambda x:x+1)==types.LambdaType)

#判断是否是函数
print(type(fn)==types.FunctionType)
#判断是否是generator
print(type((x*x for x in range(1000)))==types.GeneratorType)
#判断是否是itretor
print(type([x*x for x in range(1000)])==list)
print(type([x*x for x in range(1000)]))
"""
如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
"""
print(dir('1111'))


class myObject(object):
    def __init__(self):
        self.x=9


    def power(self):
        return  self.x*self.x

"""
仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
"""
obj =myObject()
print(hasattr(obj,'x')  )
setattr(obj,"y",10)
print(hasattr(obj,"y"))
print(getattr(obj,"z",100))

"""
finished!
"""


