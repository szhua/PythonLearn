

#枚举

from enum import Enum ,unique

"""
value属性则是自动赋给成员的int常量，默认从1开始计数。
"""
leilei =Enum("Leilei",("szhua","szhua2"))

for x in leilei:
    print(x)

print(leilei.__members__.items())

@unique
class Weekday(Enum):
    SUN=0
    MON=1
    TUE=2
    WED=3
    TUR=4
    FRI=5
    SAT=6

print(Weekday.SUN.name)



