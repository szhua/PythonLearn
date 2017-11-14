#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
test()


"""
关于__name__这个变量
直接使用本模块进行运行的时候显示的是__main__
但是当被别的模块引用的时候 import的时候
现实的便是 sys.argv[0] 即当前模块的名称；
"""
if __name__=='__main__':
    test()
else :
    print(__name__)