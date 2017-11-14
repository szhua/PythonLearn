
#测试下 property属性
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self, value):
        if not isinstance(value, int):
            #抛出异常
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
    pass


# leilei =Student()
# leilei.set_score("1111")


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value


    @property
    def height(self):
        return self._height

    @width.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width*self._height


screen =Screen()
screen.width=100
screen.height =90
print(screen.resolution)














