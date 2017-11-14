



class Student(object):

    #先进行set的方法
    @property
    def score(self):
        return  self._score

    #然后写set的方法；
    @score.setter
    def score(self,value):
     self._score =value


s =Student()
s.score=10
print(s.score)


class Screen(object):
    @property
    def width(self):
          return self._width
    @width.setter
    def width(self ,value):
        if isinstance(value, int) and value > 0:
             self._width =value ;
        else:
            raise ValueError("error")
    @property
    def height(self):
        return  self._height
    @height.setter
    def height(self,value):
        self._height =value
    @property
    def resolution(self):
        return self._height * self._width
    pass

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432
print('1024 * 768 = %d ' % s.resolution)

from Unit2.Lesson9 import Hello

hello = Hello()
print(type(Hello))
print(type(hello))
print(type(Hello))











