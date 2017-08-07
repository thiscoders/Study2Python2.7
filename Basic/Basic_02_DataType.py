# coding=utf-8
# !/usr/bin/env python2.7

# 1.整数
print '--------整数--------'
print 100 + 200

# 2.浮点数
print '--------浮点数--------'
fnum = 2.345
print 1.234 + fnum

# 3.字符串
print '--------字符串--------'
print "I'm ok"
print 'Hello world'

# 4.转义字符
print '--------转义字符--------'
# 尝试输出 \n  \r  \  '  ''
print '\\n', '\\r', 'lala', '\\', '\'', '\'\''
print r'\\\t\\\n\\'  # 可见\t\n没有变成换行,实现对一行所有特殊字符的转义
print '''
    多行输入
    123
    啦啦啦
'''  # 输出多行内容

# 5.布尔运算
print '--------布尔运算--------'
print 'True and True is ', True and True
print 'True and False is ', True and False
print 'False and False is ', False and False, '\n'

print 'True or True is ', True or True
print 'True or False is ', True or False
print 'False or False is ', False or False, '\n'

print 'not True is ', not True
print 'not False is ', not False, '\n'

# 布尔值可以用于条件判断控制流程

# 6.空值None
# iinum = raw_input('这里什么都别输入:') #去掉这个注释就会走第一个判断
print '--------空值--------'
iinum = None
if iinum is None:
    print '你刚刚输入了空值！'
else:
    print '你刚刚没有输入空值！'

# 7.变量 注：python是一种弱类型的语言，即一个变量不仅可以保存整数也可以保存字符串，还可以保存float
print '--------变量--------'
vnum = raw_input('请输入：')
print vnum

# 8.常量 固定不变的变量，通常用大写表示,比如：
print '--------常量--------'
PI = 3.1415928
NAME = '小明'

# 9.除法&取余
print '--------除法&取余--------'
print '10/3=', 10 / 3, ' 10.0/3=', 10.0 / 3  # 除法
print '10%3=', 10 % 3  # 取余
