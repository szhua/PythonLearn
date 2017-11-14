



path ="C:\\Users\\Administrator\\Desktop\\gitCode.txt"

with open(path,"w+",encoding="utf8") as f:
      f.write("Hello Python!!!")
      pass

with open(path,"r",encoding="utf8") as f:
      lines =f.readlines()
      for x in lines:
          print(x)


"""
StringIo
BytesIo
"""

from io import  StringIO
from io import  BytesIO

strIo =StringIO()
strIo.write("Hello leilei")
print(strIo.getvalue())
print(type(strIo.readlines()))

f =BytesIO()
f.write("你好蕾蕾".encode("utf-8"))
print(f.getvalue())

#weindows不能查询uname这个变量
import os
if "nt"!=os.name:
    print(os.uname())
#打印环境变量
print(os.environ)

#查看当前目录的绝对lujing
print(os.path.abspath("."))
abs_path =os.path.abspath(".")

base_path ="C:\\Users\\Administrator\\Desktop\\"

"""创建路径=》创建新的文件夹"""
# import  logging
#
# path =os.path.join(base_path,"szhua")
# #存在就删除不存在就创建；；；
# os.rmdir(path) if os.path.exists(path) else os.mkdir(path)


file ="C:\\Users\\Administrator\\Desktop\\d"



print(os.path.isdir(file))
#写一个列表生成器
dir = [ x for x in os.listdir(base_path) if os.path.isdir(base_path+x)and x.startswith("p") ]
print("=======")
for x in dir:
    print(x)
print("Android Studio.lnk".startswith("A"))

