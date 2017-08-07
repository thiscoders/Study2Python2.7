# -*- coding: utf-8 -*-

# 线程(Thread)是计算机程序的最小单位，n多线程组成了一个进程(Process)

# python标准库提供了两个模块thread和threading，前者是低级模块，threading是高级模块（对thread进行了封装），多数情况下只需要使用threading这个模块

import time, threading


# 新线程执行的代码
def loop():
    # current_thread()永远返回当前线程的实例
    print 'threading %s is begin...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(2)
    print 'thread %s ended...' % threading.current_thread().name


print 'thread (%s) is running...' % threading.current_thread().name
# 定义新的线程  target指定线程要执行的代码，name是子线程的名字
t = threading.Thread(target=loop, name='LoopThread')
t.start() # 开始线程
t.join()  # 使主线程等待子线程
print 'thread (%s) ended.' % threading.current_thread().name
