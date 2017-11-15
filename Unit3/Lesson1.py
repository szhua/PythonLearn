
#学习正则表达式：
#在正则表达式中，如果直接给出字符，就是精确匹配。用\d可以匹配一个数字，\w可以匹配一个文字
#.可以匹配任何字符


import  re

#若是匹配成功的情况下回返回一个match对象

#
print(re.match(r"^\d{3}\-\d{3,8}","010-9090"))
#<_sre.SRE_Match object; span=(0, 8), match='010-9090'>
print(re.match(r"\d{3}\-\d{3,8}","010-11"))
#None 则为不匹配；

#直接使用if 进行判断match的结果：
if(re.match(r"^\d{3}\-\d{3,8}","010-9090")):
    print("match ok !!")
else:
    print("not match!!")
if(re.match(r"^\d{3}\-\d{3,8}","010-90")):
    print("match ok !!")
else:
    print("not match!!")

#使用正则进行切割字符串：

#正常的做法
print( "a v c ".split(" "))
#r"\s+" 直接分割开带有至少带有一个空格的
print(re.split(r"\s+","a v c  d   f"))

#将多个空格，含有，的分割开来
print(re.split(r"[\s\,]+","a v c d , f"))

print(re.split(r"[\s\,\;]+","a v c ,;d ;;,f"))


"""分组"""
#[里面的表示可选] {表示数量} (表示分组)
#除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group

m =re.match(r"^(\d{3})\-(\d{3,8})$","010-90909909")
print(m.group(0))
print(m.group(1))
print(m.group(2))
t = '01:05:30'
#r"^(0[0-9]|1[0-9]|2[0-3]|[0-9])" 时分秒分别进行判定！！ext:小时的判定；+匹配前面的子表达式一次或多次
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())


# '^(\d+)(0*)$' 出现一次或多次的数字  以0结尾 ==》贪婪原则直接返回('102300', '')
m= re.match(r'^(\d+)(0*)$', '102300').groups()
print(m)

#解决方案：最小匹配原则
m =re.match(r"^(\d+?)(0*)$","102300").groups()
print(m)

"编译"

"""
当我们在Python中使用正则表达式时，re模块内部会干两件事情：
1/编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
2/用编译后的正则表达式去匹配字符串。
"""

pattern =re.compile(r"^(\d+?)(0*)$")
print(pattern.match("1023000").groups())
#邮箱的正则表达式；
pattern =re.compile(r"^([a-zA-Z\.]+)\@([a-zA-Z0-9]+)\.([a-zA-Z]{3})$")

print(pattern.match("someone@gmail.com").groups())


#提取带名字的； 注意中间可能会有空格
#<Tom Paris>tom@voyager.org
pattern =re.compile(r"^\<([a-zA-Z0-9\s]+)\>\s*([a-zA-Z0-9]+)\@([a-zA-Z0-9]+)\.([a-zA-Z]{3})$")

if pattern.match("<Tom Paris> tom@voyager.org"):
    print(pattern.match("<Tom Paris> tom@voyager.org").groups())
else:
    print("NOT OK!")



