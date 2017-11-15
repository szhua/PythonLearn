

#并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。


class Leilei(object):

    def __init__(self ,name):
        self.name=name

#"""实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如，下面的class实现了这两个方法："""

    def __enter__(self):
        print("Leilei")
        return  self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def shuo(self):
       print("my name is",self.name)



with Leilei("LEILEI") as leilei:
      leilei.shuo()



