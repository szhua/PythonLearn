
# import  time
#
# def reader():
#      """A generator that fakes a read from a file, socket, etc."""
#      for i in range(101):
#          yield '<< %s' % i
#
# def consumer():
#     r = ''
#     while True:
#         #但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。
#         #此处的n是接受参数
#         n = yield from  reader()
#         print("===",n)
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 100:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
# c = consumer()
# produce(c)


# def getIN():
#     for x in range(1000):
#        n = yield x
#        print(n,"--rer",x)
#
# ge =getIN()
#
# #开始
# ge.send(None)
# ge.send("11")
# ge.send("222")

def accumulate():    # 子生成器，将传进的非None值累加，传进的值若为None，则返回累加结果
     tally = 0
     while 1:
         next = yield
         if next is None:
             return tally
         tally += next



def gather_tallies(tallies):    # 外部生成器，将累加操作任务委托给子生成器
       while 1:
           tally = yield from accumulate()
           tallies.append(tally)

tallies = []
acc = gather_tallies(tallies)
next(acc)    # 使累加生成器准备好接收传入值
for i in range(4):
   acc.send(i)

acc.send(None)    # 结束第一次累加
for i in range(5):
   acc.send(i)




acc.send(None)    # 结束第二次累加
print(tallies)

def get():
    n =1
    while True:
        n+=1
        if n>10:
            break
        yield

for x in get():
    print(x)
