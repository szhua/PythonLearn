#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#网站的基本框架
import  logging ;

#设置日志级别
logging.basicConfig(level=logging.INFO)

import  asyncio ,os ,json ,time
from datetime import  datetime
from  aiohttp import web

#请求首页界面
def index(request):
    return  web.Response(body="df发动机康师傅框架".encode(encoding="gbk"),headers={"content-type":"text/html"})

async def init(loop):
    #创建app;
    app =web.Application(loop=loop)
    # params: method .path ,function
    app.router.add_route('GET','/',index)
    #
    srv =await  loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return  srv

loop =asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

