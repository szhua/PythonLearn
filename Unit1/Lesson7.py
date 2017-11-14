#列表生成器

arrary =list(range(1,11))
print(arrary)

arrary =[x*x for x in range(1,11) if x%2 ==0]
print(arrary)

arrary =[m+n for m in "ABCSD" for n in "af"]
#C52

print(arrary)


import  os
#列举当前目录下的数据
arrary=[dir for dir in os.listdir('.')]
print(arrary)

print(os.listdir("."))




