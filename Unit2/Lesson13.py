
#对象的序列化：

import pickle
#写入文件
d =dict(szhua=111,name=111)
print(pickle.dumps(d))
f =open("dump.txt","wb")
pickle.dump(d,f)
f.close()
#读取对象
f =open("dump.txt","rb")
d=pickle.load(f)
f.close()
print(d)



import  json

szhua={"shzu":11}

print(json.dumps(szhua))

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Bob', 20, 88)

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


"""
利用object的.__dict__属性获得一个dict ；；；
当然处理含有__slots__属性的除外
"""
json_str =json.dumps(s,default=lambda object:object.__dict__)
print(json_str)
#object =json.loads(json_str,object_hook=lambda d:Student(d["name"],d["age"],d["score"]))

"""先将jsonStr转换成dict 然后将dict转换成对象"""
object=json.loads(json_str,object_hook=dict2student)
print(object.name)























