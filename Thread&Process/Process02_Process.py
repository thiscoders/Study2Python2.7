# -*- coding: utf-8 -*-
'''
由于上一个例子只能运行在unix/linux环境下，所以Python也提供了跨平台的多进程支持
multiprocessing模块就是跨平台版本的多进程模块。
multiprocessing模块提供了一个Process类来代表一个进程对象
'''
from multiprocessing import Process
import os, time


def run_proc(name):
    print 'func is running...'
    for i in range(5):
        print '%s,run child process %s (%s)' % (i, name, os.getpid())
        time.sleep(500)


if __name__ == '__main__':
    print 'parent process is %s ' % os.getpid()
    # 定义一个进程
    p = Process(target=run_proc, args=('test',))
    print 'process begin...'
    # 开始子进程
    p.start()
    p.join()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print 'process end...'
