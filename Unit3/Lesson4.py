


#base64

#1、先准备64个字符list
#2、然后，对二进制数据进行处理，每3个字节一组
#3、共是3x8=24bit，划为4组，每组正好6个bit：
#4、然后正好对应的是64个数，2的6次方

print("ceshi")
"""
所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。

如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

Python内置的base64可以直接进行base64的编解码：
"""

import  base64

#\x00在这里代表的一个一个字符
encode =base64.b64encode(b'szhua\x00string')
print(encode)
print(base64.b64encode(b"szhua"))

print(base64.b64decode("YWJjZA=="))


#不带==的解码 b
def safe_base64_decode(s):
    #若是bytes
    if isinstance(s,str):
        #将bytes转换成str
      s=b""+s
    #计算长度
    yu = len(s)%4
    return base64.b64decode(s+b"="*yu)

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')



"简单点的Str"
#不带==的解码
def safe_base64_decode(s):
    #若是bytes
    if isinstance(s,bytes):
        #将bytes转换成str
      s =str(s,encoding = "utf-8")
    #计算长度
    yu = len(s)%4
    return base64.b64decode(s+"="*yu)

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')
