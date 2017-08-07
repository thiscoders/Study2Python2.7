# coding=utf-8
# !/usr/bin/env python2.7

print '--------字符编码--------';
print '--------字符==>数字--------';
vnum = ord('A');
print vnum;

print '--------数字==>字符--------';
vchar = chr(65);
print vchar;

print '--------Unicode表示字符--------';
print u'这是Unicode表示的字符';
print(u'这是Unicode表示的字符', 213);

print '--------Unicode==>UTF-8--------';
res = u'你好'.encode('utf-8');
print(res);
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8');

print '--------格式化输出--------';
# python中字符串格式化和c是一致的
print '你好,%s,你的年龄是%d' % ('小明', 18);
print '整数%d，浮点数%f，字符串%s，十六进制整数%x' % (102, 23.541, 'lalala', 23);
# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print '%d and %02d and %03d' % (1, 1, 1);
print '%.2f and %.3f' % (3.1415926, 3.1415926);
# %s永远是万能药
print '%s and %s' % (3.134, True);
# 百分数表示法
print '%d%%' % (7);

print '--------数字==>字符--------';
