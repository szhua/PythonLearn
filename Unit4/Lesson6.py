
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hell, %s!</h1>' % (environ['PATH_INFO'][1:] or 'Lesson6')
    return [body.encode(encoding='utf-8')]


# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')

# 开始监听HTTP请求:
httpd.serve_forever()





