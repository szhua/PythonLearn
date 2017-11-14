

"""
全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。
你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，
可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
"""
#解决线程间变量相互影响的问题

import  threading

thread_local =threading.local()

class Student(object):

    def __init__(self,name):
        self.name=name
        pass

def process_student():
    #使用当前线程的student对象
    std =thread_local.stu
    print("Hello %s in thread(%s)"%(std.name,threading.current_thread().name))

def process_thread(name):
    #为当前线程设置对象
    thread_local.stu =Student(name)
    process_student()


if __name__ == '__main__':
    t1 =threading.Thread(target=process_thread,args=("Szhua",),name="Thread_A")
    t2 =threading.Thread(target=process_thread,args=("Leilei",),name="Thread_B")
    t1.start()
    t2.start()
    t1.join()
    t2.join()

"""
一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
"""


