



#python解析xml;


from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):

    def start_element(self,name,attrs):
        print("sax  start element name: %s ,attrs: %s" %(name,str(attrs)))
    def end_element(self,name):
        print("sax end element name:%s" % name)
    def data(self ,data):
        print("sax data ====%s " %data)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">附近的时刻附近说的
    发的啥了法律手段
    fdskflsdfk</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

parser =ParserCreate()
handler =DefaultSaxHandler()

#函数的绑定
parser.StartElementHandler  =handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.data

print(parser.CharacterDataHandler)
#parser.Parse(xml)




#具体逻辑处理对象；







import re

class WeatherSaxHandler(object):
    #定义解析成json的属性
    def __init__(self) :
        self.city =""
        self.county=""
        self.weathers=[]

     #解析数据
    def start_element(self ,name ,attrs):

          weather_regex = re.compile(r"yweather\:(\w*)")
          y_match =weather_regex.match(name)
          if y_match:
           print(y_match.group())




          if attrs!=None and attrs.__contains__("city"):
              self.city =attrs['city']
              self.county =attrs['country']
          if attrs!=None and attrs.__contains__("day"):
              self.weathers.append(attrs)
    def end_element(self,name):
         pass
    def data(self,text):
        pass

import json
def parse_weather(xml):
    weatherParser = ParserCreate()
    weatherhandler = WeatherSaxHandler()
    weatherParser.StartElementHandler = weatherhandler.start_element
    weatherParser.EndElementHandler = weatherhandler.end_element
    weatherParser.CharacterDataHandler = weatherhandler.data
    weatherParser.Parse(xml)
    # 解析成json ;;;;
    return json.dumps(weatherhandler, default=lambda obj: obj.__dict__)


# 测试:
data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''

print(parse_weather(data))








