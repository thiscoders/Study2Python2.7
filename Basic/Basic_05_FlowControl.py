# coding=utf-8
# !/usr/bin/env python2.7

# python 流程控制
# 1.判断结构 ，只要满足第一个条件剩下的语句都不会被执行
age = 20;
if age < 18:
    print '你的年龄小于18岁';
elif age > 18 and age < 25:
    print '你还很年轻';
elif age > 25:
    print '你要奔3了';
else:
    print '你是老鸟';

# if 的简略写法 if后面的表达式不是0，不是None就判断为True ，否则就是False
if 'a':
    print 'ok';
if None:
    print 'not';
"""
anum = raw_input('anum:');
bnum = raw_input('bnum:');
print int(anum) + int(bnum);
"""
# 2.循环结构

# a.for循环
for v in (1, 2, 3, 4, 5):  # 遍历元组，列表
    print v;

rnum = range(5);
print rnum;

for vn in range(1, 3):
    print vn;

# b.while循环

while True:
    wnum = int(raw_input('是否结束：'));
    if wnum < 0:
        break;
    print '你好';

# 例子1：1到100求和
nsum = 0;
for x in range(101):
    nsum = nsum + x;
print nsum;
