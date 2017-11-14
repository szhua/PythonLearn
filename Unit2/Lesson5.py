
class Student(object):
    pass


def setAge(self ,age):
    self.age =age

szhua =Student()




from types import MethodType


##为一个实例绑定方法
szhua.set_age =MethodType(setAge,szhua)

szhua.set_age(10)

print(szhua.age)

#为了给所有实例都绑定方法，可以给class绑定方法
Student.set_age =setAge

leilei =Student()
leilei.set_age(10)
print(leilei.age)

#如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。 __slots__限制外部添加
class Student(object):
    __slots__ = ('name', 'age',"setAge")
    pass
蕾蕾 =Student()
蕾蕾.setAge =MethodType(setAge,蕾蕾)
蕾蕾.setAge(10)
print(蕾蕾.age)































