

#
"""
定制函数
"""

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
leilei =Student('leilei')
print(leilei)


class Fib(object):
    def __init__(self) -> None:
       self.a,self.b =1,1
    def __iter__(self):
        return  self

    def __next__(self):
        self.a ,self.b =self.b,self.a+self.b
        if self.a>100000:
            raise  StopIteration()
        return  self.a
    def __getitem__(self, n):
       for i in range(n):
           self.a ,self.b =self.b ,self.a+self.b
       return  self.a ;
print(Fib()[100])
print(Fib()[100])
# for i in Fib():
#     print(i)
f =list(Fib())
print(f[:10:2])

class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        #%%s将字符串相互联系在一起
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    def users(self,value):
        return Chain("%s%s"%(self._path,value))
    __repr__ = __str__

print(Chain().users('michael').repos)



class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)




leilei =Student("leilei")
leilei()

