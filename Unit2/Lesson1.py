
#Class ！！！
"""
在函数内部的属性名前加__可以让内部属性不被访问
可以在类中增加方法让外部代码获取、修改类的内部属性
"""
class Student(object):

#get set方法‘
    def set_name(self ,name):
        self.__name =name
    def get_name(self):
        return  self.__name


    def __init__(self,name,score):
       self.__name  =name
       self.__score =score

    def getInfo(self):
        print(self.__name,self.__score)
    pass


szhua =Student("szhua",190)
leilei =Student("leilei",200)
leilei.age =24

#访问他的name属性；
print(leilei.get_name())
print(leilei.age)


"""
面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。
Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，
而实例（Instance）则是一个个具体的Student，比如，Bart Simpson和Lisa Simpson是两个具体的Student。
"""