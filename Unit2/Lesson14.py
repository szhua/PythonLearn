# #!/usr/bin/env python3
# # -*- coding: gbk -*-
#
# from multiprocessing import Process
# import os
#
# # 子进程要执行的代码
#
# def runOs(name):
#     print("Run child process name:%s(%s)"%(name,os.getpid()))
#     pass
#
# if __name__=="__main__":
#     print("current process:" + os.name + str(os.getpid()))
#     #创建进程
#     p=Process(target=runOs,args=("test",))
#     #开始进程
#     p.start()
#     #结束进程
#     p.join()
#     print('Child process end.')
#
# """
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
# """
#
#
# #使用进程池进行多进程任务
# from multiprocessing import Pool
# import  time,random,os
# #执行进程任务：：
# def long_time_task(name):
#   print("current task process name:%s(pid:%s)"%(name,os.getpid()))
#   start=time.time() ;
#   time.sleep(random.random()*3)
#   end =time.time()
#   print("process all takes %0.2f 毫秒"%(end-start))
#
# if __name__=="__main__":
#     print("the main process name:%s pid:%s"%(os.name,os.getpid()))
#     #创建进程池
#     p =Pool(4)
#     for x in range(5):
#     #异步地执行进程任务
#      p.apply_async(long_time_task,args=(x,))
#
#     print("waiting for async process done")
#     p.close()
#     #子进程结束后再继续往下运行
#     p.join()
#
# """
# 注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，
# 这是因为Pool的默认大小在我的电脑上是4，
# 因此，最多同时执行4个进程。这是Pool有意设计的限制，
# 并不是操作系统的限制。如果改成：
# """
# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.liaoxuefeng.com'])
# print('Exit code:', r)



#进程间的通讯：


from multiprocessing import Queue,Process

import  os ,time ,random

def write(q):
  print("process to write: ",os.getpid())
  for value in ["A","B","C","D","C"]:
      print("prosss: %s put value: %s"%(os.getpid(),value))
      q.put(value)
      time.sleep(random.random())

def read(q):
   print("process to read：",os.getpid())
   while True:
         value =q.get(True)
         print("pross:%s readValue: %s"%(os.getpid(),value))

if __name__ == '__main__':
 q =Queue()
 "注意构造参数：：：！！！"
 pw = Process(target=write,args=(q,))
 pr = Process(target=read,args=(q,))
 pw.start()
 pr.start()
 pw.join()
 pr.terminate()
 print("end!!")
 #pr进程里是死循环，无法等待其结束，只能强行终止:
# pr进程里是死循环，无法等待其结束，只能强行终止:




