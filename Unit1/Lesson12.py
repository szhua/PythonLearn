#重新学习Python filter()

"""字数的求发"""

def createData():
    n=1
    yield 2
    while True :
        n=n+2
        yield n

def isVislble(n):
    return lambda x:x%n!=0

#求；

def primes():
    t =createData()
    while True:
       n =next(t)
       yield  n
       t=filter(isVislble(n),t)
       if(n>1000):
           break


# print(list(primes()))
# #12321
#
# def judge(n):
#     s =str(n)
#     return  list(map(lambda x:s[x]==s[len(s)-x-1],range(0,int(len(s)/2))))
#
#
# def check(n):
#     s =str(n)
#     return s ==s[::-1] and n>10
# print(list(filter(check,range(1,1000))))

#
#
# def result(n):
#     for i in judge(n):
#         if i ==False:
#             return  False
#     return  True
# print(list(filter(result,range(1,10000))))
#
# # print("12345678"[::2])
#
# print([1,2,3,4,5,6][::-1])


# def is_palindrome(n):
#     return abs
#
# print(is_palindrome(101)(11))
# print(list(filter(is_palindrome,range(1,1000))))


L = [('Bob', 75), ('adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L,key=lambda x:x[1]))