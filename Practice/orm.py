


import logging

import aiomysql ,asyncio



class Field(object):
    def __init__(self ,name,column_type,primary_key,default):
        self.name=name
        self.column_type =column_type
        self.primary_ley =primary_key
        self.default =default
    def __str__(self):
        return "<%s,%s:$s>"%(self.__class__.__name__,self.column_type,self.name)
class StringField(Field):
    def __init__(self,name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super.__init__(self,name,ddl,primary_key,default)
class IntegerField(Field):
    def __init__(self,name=None,primary_ley=False,default=0,ddl="bigint"):
        super.__init__(self,name,ddl,primary_ley,default)
class FloatFiled(Field):
    def __init__(self,name=None, primary_key=False, default=0.0):
        super.__init__(self,name,"real",primary_key,default)
class BooleanField(Field):
    def __init__(self,name=None,primary_key=False,default=False):
        super.__init__(self,name,"boolean",primary_key,default)
class TextField(Field):
    def __init__(self, name=None, primary_key=False, default=None):
        super.__init__(self, name, "text", primary_key, default)

def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)


#metalclass 使用元类对class 进行处理
class ModeMetalClass(type):
    # bases继承关系
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls, name, bases, attrs)
        #获得表名 不存在的话就设置为类名
        tableName =attrs.get('__table__',None) or name
        logging.info("find model %s ,table(name:%s)"%(name,tableName))
        mapping=dict()
        fileds=[]
        primary_key =None
        for k,v in attrs.items():
            if(isinstance(k,Field)):
                logging.info("find mapping %s==>%s"%(k,v))
                mapping[k] =v
                #若是含有主键的情况下 filed.primary_ley:
                if v.primary_key:
                    #检查是否含有上一个主键
                    if primary_key:
                        raise  BaseException("主键个数大于一个 %s"%primary_key)
                    #为主键赋值==id ,name ,pic
                    primary_key=k
                else:
                    #除了主键以外的键存在fields中
                    fileds.append(k)
                #主键不存在的情况下
                if not primary_key :
                    raise  BaseException("Primary key not found.")
                #防止运行时错误的产生
                for k in mapping :
                    attrs.pop(k)
                #转换成sql语句中需要的字段：
                ecscaped_fields=map(lambda f:"'%s'"%f,fileds)
                attrs["__mapping__"]=mapping
                attrs["__table__"]=tableName
                attrs["__primary_key__"]=primary_key
                attrs["__fields__"]=fileds #除了主键以外的键名称
                attrs["__select__"]='select `%s` ,`%`s from `%s`'%(primary_key,",".join(ecscaped_fields),tableName) #select 语句 ————查找全键
                #TODO
                attrs["__insert__"]='insert into `%s` (`%s`,`%s`) values (`$s`)'%(tableName,primary_key,",".join(ecscaped_fields),create_args_string(len(ecscaped_fields)-1))
                #TODO
                attrs["__update__"]='update `%s` set `%s` WHERE  `%s`=?'% (tableName,",".join(map(lambda f: '`%s`=?' % (mapping).get(f).name or f)),primary_key)
                attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primary_key)
                return  type.__new__(cls,name,bases,attrs)

class Model(dict,metaclass=ModeMetalClass):

 pass





