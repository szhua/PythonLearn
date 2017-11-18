

#HTML parser

from html.parser import HTMLParser
import  json

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('==startTag==<%s>' % tag)

    def handle_endtag(self, tag):
        print('==endTag==</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('==stasrtendTag==<%s/>' % tag)

    def handle_data(self, data):
        print("data==%s"%data)

    def handle_comment(self, data):
        print('==comment==<!--', data, '-->')

    def handle_entityref(self, name):
        print('==entityref==&%s;' % name)

    def handle_charref(self, name):
        print('==charref==&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')



"""
  <li>
                        <h3 class="event-title"><a href="/events/python-events/571/">PyConAr 2017</a></h3>
                        <p>
<time datetime="2017-11-17T00:00:00+00:00">17 Nov. &ndash; 20 Nov. <span class="say-no-more"> 2017</span></time>
                            <span class="event-location">Haya De La Torre S/N, Córdoba, Cordoba, Argentina</span>
                            
                        </p>
                    </li>
"""

"爬取python官网的大事件"
from html.parser import HTMLParser
import  json
#判断标签
def get_attr(attrs, attrs_name,attrs_value=""):
    for attr in attrs:
        if attr[0] == attrs_name:
            if attrs_value=="":
                return  True
            if attr[1]==attrs_value:
                return  True
    return False
#输出Python官网发布的会议时间、名称和地点。
class EventHtmlParser(HTMLParser,list):
    title =False
    time =False
    location =False
    event =dict()
    def handle_starttag(self, tag, attrs):
        if tag =="h3" and  get_attr(attrs,"class","event-title"):
            self.title =True
        elif tag=="time" and get_attr(attrs,"datetime"):
            self.time =True
        elif tag=="span" and get_attr(attrs,"class","event-location"):
            self.location =True
    def handle_startendtag(self, tag, attrs):
        pass
    def handle_data(self, data):
        if self.title:
            self.event["title"]=data
            self.title=False
        if self.time:
            self.event["time"]=data
            self.time =False
        if self.location :
            self.event["location"]=data
            self.location =False
            self.append(self.event)
            self.event=dict()
    def handle_endtag(self, tag):
     pass
    def handle_startendtag(self, tag, attrs):
      pass
    def handle_comment(self, data):
      pass
    def handle_entityref(self, name):
      pass
    def handle_charref(self, name):
       pass

from urllib import request
with request.urlopen('https://www.python.org/events/python-events/') as f:
    data = f.read()
eventParser =EventHtmlParser()
eventParser.feed(data.decode('utf-8'))
print(json.dumps(eventParser))






