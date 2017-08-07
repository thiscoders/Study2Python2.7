# coding=utf-8
# !/usr/bin/env python2.7
import logging

print 'start'
try:
    print 10 / 0
    print 'goon...'
except ZeroDivisionError, e:
    print '----->>>exception occor:', e
    #logging.exception(e) # 填上这句话，程序可以正常的走完
finally:
    print 'this is finally...'
print 'end'


# Python的错误其实也是class，所有的错误类型都继承自BaseException.
# 在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。
# Python内置的logging模块可以非常容易地记录错误信息：
# logging还可以把错误记录到日志文件里，方便事后排查

'''
try:
    ...
except ...Error,e:
    ...
finally:
    ...
'''