# coding=utf-8
# !/usr/bin/env python2.7

import re
# Python 正则表达式的使用
'''
常用符号：
    .:匹配任意字符（占位符），除了换行符\n
    *:匹配前一个字符0次或者无限次
    ?:匹配前一个字符0次或者1次
    .*:贪心算法
    .*?:不贪心算法
    ():括号内的数据作为结果返回
常用方法：
    finddall():匹配所有符合规律的内容，返回包含结果的列表
    search():匹配整个字符串，直到找到一个匹配
    match():只匹配字符串的开始，匹配失败返回None
    sub():替换符合规律的内容，返回替换后的值
正则表达式修饰符:
    re.I,re.L,re.M,re.S,re.U,re.X    
'''
string = """hello world,hello china,hello space,hellothis.
How are you? Python is grate!
"""
flags=0

pattern_find = 'this'
pattern_search = r'(hello).(ace)'
pattern_sub = 'world'

print re.match('world',string)
print re.findall(pattern_find,string)
res_search= re.search(pattern_search,string,re.M|re.I)
if res_search:
    print res_search.group(1)
    print res_search.group(2)
else:
    print 'nothing found!'
#print re.sub(pattern,string)