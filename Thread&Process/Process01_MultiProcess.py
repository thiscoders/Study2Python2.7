# -*- coding: utf-8 -*-

# 进程是由很多线程组成的
'''
Python多任务实现的3种方式
    1.多进程模式
    2.多线程模式
    3.多进程+多线程模式
'''
import os

print 'processing (%s) start!' % os.getpid()
try:
    pid = os.fork()
    if pid == 0:
        print 'i am child process (%s),,,my parent is (%s)' % (os.getpid(), os.getppid())
    else:
        print 'i am parent(%s) and i created %s' % (os.getpid(), pid)
except Exception, e:
    print e

'''
上述代码只能执行在linux系统下，window系统无法执行，windows下没有fork
执行结果如下
processing (84) start!
85
0
'''
