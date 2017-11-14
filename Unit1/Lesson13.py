#返回函数

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


"""
f1()和f2()的调用结果互不影响。
"""
f1 =lazy_sum(1,2,3,4,5,6)
f2 =lazy_sum(1,2,3,4,5,6)
print(f1()==f2())
print(f1==f2)




def log(func):
    def wrrapper(*args,**kw):
        print("call %s()"%func.__name__)
        return func(*args,**kw)
    return  wrrapper
import  time


'''
现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，
'''


@log
def now():
    print(time.time())

now()