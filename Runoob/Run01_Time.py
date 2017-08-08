# encoding=utf-8
# !/usr/lib/env python2.7

import time

print "time&data"

# 获取毫秒数
ticks=time.time()
print 'time...',ticks

# 获取时间数组
localtime=time.localtime(ticks)
print 'localtime...',localtime

# 获取格式化的时间
formattime=time.asctime(localtime)
print 'format...',formattime

# 获取格式化日期
formatdata=time.strftime("%Y-%m-%d %H:%M:%S %a",localtime)
print 'format data...',formatdata

# 获取某年某月日历
import calendar
cal=calendar.month(2017,2)
print cal

# 列出calendar模块下所有函数
print dir(calendar)