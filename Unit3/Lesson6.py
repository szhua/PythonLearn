


#Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。


import  hashlib

#生成密码：
def get_md5(str):
    md = hashlib.md5()
    md.update(str.encode("utf8"))
    return  md.hexdigest()
#创建数据库
db={

}
#注册
def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
#注册测试用户
register("szhua","123456")
register("leilei","12222")
#登录判断
def login(username, password):
        (print("登录成功")  if db[username]==get_md5(password+username+"the-Salt") else  print("密码错误"))\
            if(db.__contains__(username)) else print("用户不存在")

login("szhua","13456")
login("szhua1","123456")
login("szhua","123456")



