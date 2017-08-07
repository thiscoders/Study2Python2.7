# -*- coding: utf-8 -*-

# 多进程和多线程的区别
# 同一个变量每一个进程都会拷贝一份，互不影响。而在多线程中所有变量有所有线程共享，所以变量可以被任何一个线程修改

import thread, multiprocessing

# 获取cpu线程数
print multiprocessing.cpu_count()
