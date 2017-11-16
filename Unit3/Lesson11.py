


from xml.parsers.expat import ParserCreate
import re ,enum,json

#创建枚举便于查询
@enum.unique
class WeekDay(enum.Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


class WeatherParserHandler(dict):
# <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            #<yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
# <yweather:location city="Beijing" region="" country="China"/>
#<yweather:location city="Beijing" region="" country="China"/>
    def end_element(self, name):
     pass


    def data(self, text):
     pass

    def start_element(self ,name ,attrs):
     weather_regex =re.compile(r"yweather\:(\w*)")
     weather_match =weather_regex.match(name)
     #符合条件的情况下：
     if weather_match:
         group_mark =weather_match.group(1)
         if group_mark=="location":
             self['city']=attrs["city"]
             self['country']=attrs["country"]
         #检查日期
         elif group_mark=="condition":
            today =str(attrs['date']).split(",")[0]
            if WeekDay[today]:
                self.__today =WeekDay[today].value
                #不是星期六的情况下
                if self.__today!=6:
                 self.__tomorrow=self.__today+1
                 #星期六的情况下
                else:
                 self.__tomorrow=0
            pass
         #检查天气
         elif group_mark=="forecast" :
            #创建二级字典
            attr =dict()
            if WeekDay[attrs["day"]].value==self.__today:
                attr["low"]=int(attrs["low"])
                attr["high"] = int(attrs["high"])
                attr['text'] =attrs['text']
                self["today"]=attr
            elif WeekDay[attrs["day"]].value==self.__tomorrow:
                attr["low"] = int(attrs["low"])
                attr["high"] = int(attrs["high"])
                attr['text'] = attrs['text']
                self["tomorrow"]=attr




def parse_weather(xml):
    weather_parser =ParserCreate()
    weather_handler =WeatherParserHandler()
    weather_parser.StartElementHandler = weather_handler.start_element
    weather_parser.EndElementHandler = weather_handler.end_element
    weather_parser.CharacterDataHandler = weather_handler.data
    weather_parser.Parse(xml)
    return  weather_handler
    return json.dumps(weather_handler)



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
weather = parse_weather(data)
assert weather['city'] == 'Beijing', weather['city']
assert weather['country'] == 'China', weather['country']
assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
assert weather['today']['low'] == 20, weather['today']['low']
assert weather['today']['high'] == 33, weather['today']['high']
assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
print('Weather:', str(weather))