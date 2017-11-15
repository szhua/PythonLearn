

#从本章开始学习一下python内置的模块

from datetime import  datetime
#打印当前时间
now =datetime.now()
print(now)
print(type(now))

#指定日期:时间
time =datetime(year=2017,month=11,day=11)
print(time)

#时间戳的问题---打印时间戳
print(time.timestamp())

timestamp =datetime.now().timestamp()
#时间戳转换城日期：
print(datetime.fromtimestamp(timestamp))

#datetime也可以转换成标准的utc
timestamp =datetime.now().timestamp()
#打印本地时间
print(datetime.fromtimestamp(timestamp))
#>>2017-11-14 17:09:37.146078
#打印UTC时间
print(datetime.utcfromtimestamp(timestamp))
#>>2017-11-14 17:09:37.146078

#str转换为datetime ==>转换成时间戳
print(datetime.strptime("1993-09-12 23:30:00","%Y-%m-%d %H:%M:%S").timestamp())


#datetime转换为str
print(datetime.strftime(datetime.now(),"%Y-%m-%d %H|%M|%S"))

from datetime import timedelta

#datetime加减
now =datetime.now()
print(now)
print(now+timedelta(hours=1))
print(now-timedelta(days=90))


#时区的问题
from datetime import  timezone

tz_utc_8 =timezone(timedelta(hours=8))#创建东八区的时间
now =datetime.now()
print("++++")
print(now)
#设置时区
dt =now.replace(tzinfo=tz_utc_8)
print(dt)

#2017-11-14 17:24:06.941182
#2017-11-14 17:24:06.941182+08:00
#
#格林威治时间
utc_dt  =datetime.utcnow().replace(tzinfo=timezone.utc) # 标准的时间
print("====")
print(utc_dt)
print(utc_dt.astimezone(timezone(timedelta(hours=8)))) #东八区的时间

"""
时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。
"""

