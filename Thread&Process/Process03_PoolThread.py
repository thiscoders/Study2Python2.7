# -*- coding: utf-8 -*-

# 启动大量子进程使用线程池的方式批量创建子进程
from multiprocessing import Pool

import os, time, random


def long_time_task(name):
    print 'run long time task %s (%s)' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print '%s run %0.2f seconds.' % (name, (end - start))


if __name__ == '__main__':
    print 'parent process is %s' % os.getpid()
    p = Pool()  # Pool()默认线程数是4个，p=Pool(5) 就可以同时跑5个线程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'waiting for all subprocessing done.'
    p.close()  # 调用join之前必须先调用close，调用close()之后就不能继续添加新的process了
    p.join()  # join1方法会等待所有的子进程执行完毕，常用来进行线程之间的同步
    print 'all subprocessing done'
