
#手写一个orm 框架


class Field(object):
    def __init__(self,name,column_type):
        self.name =name
        self.column_type =column_type

    def __str__(self):
        #self.__class__.__name__ ==>Filed or child's  name
        return "<%s:%s>"%(self.__class__.__name__,self.name)
pass

class StringField(Field):
    def __init__(self, name):
        super().__init__(name, "varchar(100)")
pass

class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, "bigint")
pass

szhua =StringField("szhua")
print(szhua)



class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
          if name =="Mode":
           return type.__new__(cls, name, bases, attrs)
          print("Find mode:%s"%name)
          mappings =dict()
          for k ,v in attrs.items():
              if isinstance(v,Field):
                  print("found mode value (%s:%s" % (k,v))
                  mappings[k]=v
          print(mappings)

          for k in mappings.keys():
              attrs.pop(k)


          attrs["__mapping__"]=mappings
          attrs["__table__"]=str(name).lower()
          return  type.__new__(cls,name,bases,attrs)


class Mode(dict,metaclass=ModelMetaclass):

    def __getattr__(self, item):
       try:
           return self[item]
       except KeyError:
           raise AttributeError(r"'Model' object has no attribute '%s'" % item)
    def __setattr__(self, key, value):
        self[key]=value
        pass

    def save(self):
        fields = []
        params = []
        args = []
        for k ,v in  self.__mapping__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self,k))
        sql ="insert into %s (%s) VALUES (%s) "% (self.__table__,",".join(fields),",".join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


class User(Mode):
       id =IntegerField("id")
       name =StringField("name")
       pass
leilei =User(id=1 ,name="leilei")
leilei.save()

"""
小结
metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为。这种强大的功能使用起来务必小心。
"""