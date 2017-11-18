


import  sqlite3 ,random



conn =sqlite3.connect("szhua.db")
cursor =conn.cursor()

cursor.execute("CREATE  TABLE IF NOT EXISTS leilei (id INTEGER  PRIMARY KEY AUTOINCREMENT ,name varchar(30))")

sql ="INSERT INTO leilei (name ) VALUES (\'leilei %s \') "%random.randint(90,100)

cursor.execute(sql)

cursor.close()

conn.commit()
conn.close()

#测试一下查询：

conn =sqlite3.connect("szhua.db")
cursor =conn.cursor()

cursor.execute("SELECT * FROM  leilei ")

values =cursor.fetchall()

print(values)

cursor.close()

conn.commit()
conn.close()



import os, sqlite3
from  functools import reduce

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    conn =sqlite3.connect(db_file)
    cursor =conn.cursor()
    cursor.execute("SELECT name FROM user WHERE score > %s AND score <= %s ORDER BY score ASC "%(low,high))
    values= cursor.fetchall()
    result =[]
    for x in values:
        result.append(x[0])
    cursor.close()
    conn.close()
    return  result


print(get_score_in(60,100))


assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')


