# coding=utf-8
# !/usr/bin/env python2.7

'这是一个完整的python Module代码的描述部分，这一部分是对当前模块进行描述的'

__author__ = 'ye'

import sys;

_pri01 = 100  # 私有变量

# 私有函数
def _pri_func():
    print 'pri_func is running...';


def func():
    print 'hello world!', _pri01
    _pri_func()


if __name__ == '__main__':
    print '__name__ is running...'
    func()
