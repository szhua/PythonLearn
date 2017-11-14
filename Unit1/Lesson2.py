
# # test array
# classmates =['szhua','leilei','xiaoleilei']
# print(classmates)
# print(len(classmates))
# print(classmates[2])
#
# print(classmates[-1])
# #print xiaoleilei 获得最后一个元素
# classmates.append('中国')
# print(classmates)
# classmates.insert(1,"henan")
# print(classmates)
#
# #删除最后的一个元素
# classmates.pop()
# print(classmates)
# #删除制定的元素
# classmates.pop(-1)
# print(classmates)
#
# mates =["fdsj","fff"]
# classmates[1] =mates
# print(classmates)
# ####测试不可变数组
#
# # loves =('af','ff')
# # loves[1]="ff"
# # # can error tuple object does not support item assignment!!
# # print(loves)
#
#
# t =(1)
# print(t)
#
# # would print 1
# t =(1,)
# print(t)
# # would print (1,)
##根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
age =19
if age >18 :
    print("u are audlt!!")
    print("test can print !! in if else")
age =19 ;

if age>90:
    print('you are old')
elif age>50:
    print("you are second old")
elif age>30:
    print("you are not old")
elif age>20 :
    print("you are young")
else :
    print("YOUNG!!!")

age =input("your birth")

if int(age)>=2000:
    print("00后")
else:
    print("not 00后")






