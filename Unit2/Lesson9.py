
#我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。


class Hello:
    pass

#运行时动态的创建Hello
print(type(Hello))
#调用Hello()创建出实例
print(type(Hello()))


""""
type也可以进行创建类的实例
"""

def getMyName(self,name):
    self.__name =name
    print("my name is %s!!"%self.__name)


Leilei =type("Leilei",(object,),dict(getMyName=getMyName))

leilei =Leilei()
leilei.getMyName("leilei")



"""
要创建一个class对象，type()函数依次传入3个参数：
1、class的名称；
2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
"""


"""
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
metaclass，直译为元类，简单的解释就是：
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

先定义metaclass==>然后创建类==>创建类的实例
"""
#for example:
'''1定义metalclass'''
class ListMetailClass(type):
    def __new__(cls, name, bases ,attrs):
        attrs["add"] =lambda self ,value :self.append(value)
        '''1.2.创建类'时候控制累的创建行为'''
        attrs["getALl"]=lambda self:print(attrs)

        return  type.__new__(cls,name,bases,attrs)
'''2.创建类'''
class Mylist(list,metaclass=ListMetailClass):
  pass

szhua =Mylist()
szhua.getALl()

#验证class list does‘n has attrs 'append'.
# leieli =["szhua"]
# leilei.append("leilei")
# print(leilei)

"""
__new__()方法接收到的参数依次是：

1/当前准备创建的类的对象；

2/类的名字；

3/类继承的父类集合；

4/类的方法集合。
"""

