# -*- coding: utf-8 -*-

# 进程之间相互通信 ,父进程创建共享资源
from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码
def write(q):
    for val in ['A', 'B', 'C']:
        print 'Put %s to queue...' % val
        q.put(val)
        time.sleep(random.random())


# 读进程执行的代码
def read(q):
    while True:
        val = q.get(True)
        print 'get %s from queue.' % val


if __name__ == '__main__':
    q = Queue()  # 父进程创建队列
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw
    pw.start()
    # 启动子进程pr
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程是一个while True:不能等待期结束，只能强行终止
    pr.terminate()
