#Python的多线程：




import threading ,time ,random

#在子线程中进行轮询操作
def loop():
     #显示当前线程的名字
     print("current thread name: %s"%threading.current_thread().name)
     n = 0
     while n<5:
         print("thread %s ==> %s"%(threading.current_thread().name,n))
         n+=1
         time.sleep(1)
     print("child thread is finished !!")
     pass

if __name__ == '__main__':
 #打印主线程的名字
 print("main tread name %s"%threading.current_thread().name)
 #创建子线程
 t =threading.Thread(target=loop,name="LoopThread")
 t.start()
 #执行其他的线程
 t.join()
 pass

"线程同步"

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

balance = 0

lock =threading.Lock()
def run_thread(n):
    for i in range(100):
        lock.acquire()
        try:
         print("current thread",threading.current_thread().name)
         change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

"""
当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。

获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。

##所以我们用try...finally来确保锁一定会被释放。

锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，
包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，
并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
"""

