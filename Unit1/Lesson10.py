


'''
高阶函数
'''
f=abs
print(f)
#will print : <built-in function abs> 是个内置函数
# import builtins;
# builtins.abs = 10
# print(abs)

#函数作为参数：
def add(x,y,fun):
    return  fun(x)+fun(y)
print(add(-2,3,abs))
# max, min = min, max
#
# print(max(1, 2, 3, 4, 5))
# print(min(1,2,3,4,5))
# print(list(range(0,10,2)))
max=min
print(max(1,2,3,4,5))
print(min(1,2,3,4,5))
"""
把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
"""
