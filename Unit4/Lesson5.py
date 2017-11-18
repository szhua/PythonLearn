

#mysql
#pip install mysql-connector==2.1.4
import datetime
import  mysql.connector ,random

# conn =mysql.connector.connect(user='root',password='389894467',database="leilei")
# cusor =conn.cursor()
# cusor.execute('CREATE TABLE IF NOT EXISTS szhua(id INTEGER PRIMARY KEY AUTO_INCREMENT ,name VARCHAR (30))')
# #正确的插入方法；
# cusor.execute('INSERT INTO szhua (name) values (%s) ',["leilei"+str(random.randint(10,10000))])
# conn.commit()
# conn.close()
# cusor.close()

"""
执行INSERT等操作后要调用commit()提交事务；
MySQL的SQL占位符是%s。
"""

import json
from sqlalchemy import Column, String, create_engine, INTEGER, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base =declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'
    # 表的结构:
    id = Column(INTEGER, primary_key=True,autoincrement=True)
    name = Column(String(20))
    #关联表book
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'
    id = Column(INTEGER, primary_key=True,autoincrement=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(INTEGER, ForeignKey('user.id'))


"""  dir([obj]):
    调用这个方法将返回包含obj大多数属性名的列表（会有一些特殊的属性不包含在内）。obj的默认值是当前的模块对象。
    hasattr(obj, attr): 
    这个方法用于检查obj是否有一个名为attr的值的属性，返回一个布尔值。
    getattr(obj, attr): 
    调用这个方法将返回obj中名为attr值的属性的值，例如如果attr为'bar'，则返回obj.bar。
    setattr(obj, attr, val):
    调用这个方法将给obj的名为attr的值的属性赋值为val。例如如果attr为'bar'，则相当于obj.bar = val。"""




# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:389894467@localhost:3306/leilei')
#创建表；
Base.metadata.create_all(engine)

#这个过程经历的事情
"""
>>> Base.metadata.create_all(engine)
SELECT ...
PRAGMA table_info("users")
()
CREATE TABLE users (
    id INTEGER NOT NULL, name VARCHAR,
    fullname VARCHAR,
    password VARCHAR,
    PRIMARY KEY (id)
)
()
COMMIT
"""

#解析json 用：：
from sqlalchemy.ext.declarative import DeclarativeMeta
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}


            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)     # this will fail on non-encodable values, like other classes
                    print(obj.__getattribute__(field))
                    fields[field] = data
                except TypeError:    # 添加了对datetime的处理
                    if isinstance(data, datetime.datetime):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.date):
                        fields[field] = data.isoformat()
                    elif isinstance(data, datetime.timedelta):
                        fields[field] = (datetime.datetime.min + data).time().isoformat()
                    else:
                        fields[field] = None
            # a json-encodable dict
            return fields
        return json.JSONEncoder.default(self, obj)



# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(name='Bob'+str(random.randint(0,1000)))
#创建表
new_book =Book(name="今天是个好天气"+str(random.randint(0,1000)),user_id=1)
new_book1=Book(name="今天是个好天气"+str(random.randint(0,1000)),user_id=1)
session.add(new_book1)
session.add(new_book)
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()


def jsonB(objs):
    l =[]
    for x in objs:
        l.append(x.__dict__)
    return l

session =DBSession()
users =session.query(User).filter(User.id==1).all()
print(json.dumps(users,cls=AlchemyEncoder))

