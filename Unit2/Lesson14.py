# #!/usr/bin/env python3
# # -*- coding: gbk -*-
#
# from multiprocessing import Process
# import os
#
# # �ӽ���Ҫִ�еĴ���
#
# def runOs(name):
#     print("Run child process name:%s(%s)"%(name,os.getpid()))
#     pass
#
# if __name__=="__main__":
#     print("current process:" + os.name + str(os.getpid()))
#     #��������
#     p=Process(target=runOs,args=("test",))
#     #��ʼ����
#     p.start()
#     #��������
#     p.join()
#     print('Child process end.')
#
# """
# �����ӽ���ʱ��ֻ��Ҫ����һ��ִ�к����ͺ����Ĳ���������һ��Processʵ������start()���������������������̱�fork()��Ҫ�򵥡�
# join()�������Եȴ��ӽ��̽������ټ����������У�ͨ�����ڽ��̼��ͬ����
# """
#
#
# #ʹ�ý��̳ؽ��ж��������
# from multiprocessing import Pool
# import  time,random,os
# #ִ�н������񣺣�
# def long_time_task(name):
#   print("current task process name:%s(pid:%s)"%(name,os.getpid()))
#   start=time.time() ;
#   time.sleep(random.random()*3)
#   end =time.time()
#   print("process all takes %0.2f ����"%(end-start))
#
# if __name__=="__main__":
#     print("the main process name:%s pid:%s"%(os.name,os.getpid()))
#     #�������̳�
#     p =Pool(4)
#     for x in range(5):
#     #�첽��ִ�н�������
#      p.apply_async(long_time_task,args=(x,))
#
#     print("waiting for async process done")
#     p.close()
#     #�ӽ��̽������ټ�����������
#     p.join()
#
# """
# ע������Ľ����task 0��1��2��3������ִ�еģ���task 4Ҫ�ȴ�ǰ��ĳ��task��ɺ��ִ�У�
# ������ΪPool��Ĭ�ϴ�С���ҵĵ�������4��
# ��ˣ����ͬʱִ��4�����̡�����Pool������Ƶ����ƣ�
# �����ǲ���ϵͳ�����ơ�����ĳɣ�
# """
# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.liaoxuefeng.com'])
# print('Exit code:', r)



#���̼��ͨѶ��


from multiprocessing import Queue,Process

import  os ,time ,random

def write(q):
  print("process to write: ",os.getpid())
  for value in ["A","B","C","D","C"]:
      print("prosss: %s put value: %s"%(os.getpid(),value))
      q.put(value)
      time.sleep(random.random())

def read(q):
   print("process to read��",os.getpid())
   while True:
         value =q.get(True)
         print("pross:%s readValue: %s"%(os.getpid(),value))

if __name__ == '__main__':
 q =Queue()
 "ע�⹹�����������������"
 pw = Process(target=write,args=(q,))
 pr = Process(target=read,args=(q,))
 pw.start()
 pr.start()
 pw.join()
 pr.terminate()
 print("end!!")
 #pr����������ѭ�����޷��ȴ��������ֻ��ǿ����ֹ:
# pr����������ѭ�����޷��ȴ��������ֻ��ǿ����ֹ:




