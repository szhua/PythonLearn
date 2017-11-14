#学习下python的错误处理


# try:
#   print("try...")
#   print(10/0)
# except Exception as e:
#  print('except:', e)
#  pass

import  logging
def foo(s):
    return  10/int(s)

def di(s):
    return  foo(s)*2

def main(s):
    di(s)

try:
    main("11")
except Exception as e:
   raise  e
finally:
    print("end!!")

print("leilei")


d =dict(a="szhua")
print(d["a"])

"""
们来编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问，用起来就像下面这样：
"""
class Dict(dict):
    def __getattr__(self, item):
        try:
         return self[item]
        except ValueError as e:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % item)

d =Dict(a="szhua")
print(d.a)



import unittest
class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

if __name__ != '__main__':
 unittest.main()







