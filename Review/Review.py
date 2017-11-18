
#协程


"""
概念:
子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。
协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。
"""

def consumer():
    r =''
    while True :
        n =yield  r
        if not n :
            return
        print("正在消费%s"%n)
        r ="200ok %s" %n

def produce(c):
    c.send(None)
    n  = 0
    while n<5 :
        n+=1
        print("生产 %s"%n)
        r =c.send(n)
        print("收到返回: %s"%r)

c =consumer()
produce(c)



import time
import asyncio

now = lambda : time.time()

async def do_some_work(x):
      await asyncio.sleep(2)
      print('Waiting: ', x)

start = now()

coroutine = do_some_work(2)

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)

print('TIME: ', now() - start)
print("fdsfjks")

