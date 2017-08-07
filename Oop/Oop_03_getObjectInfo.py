# coding=utf-8
# !/usr/bin/env python2.7

import types

# 获取对象信息
print '获取对象信息'
# 1. type()  所有的基本类型都可以使用type来进行判断
print '----type----'
print type(123)
print type('123')
print type(None)

print type('123') == types.StringType
print type('123') == types.NoneType
print  type(int) == type(str) == types.TypeType  # 所有类型本身的类型就是TypeType

# 2.isinstance()
print '----isinstance----'
print isinstance('123', str)
print isinstance(123, int)
print isinstance(u'123', (str, unicode))  # 判断对象是否是某一些类型中的一种,'123'是否是str或者unicode
print isinstance('123', (str, unicode))
print isinstance(123, (str, unicode))

# 3.dir() 列出对象的所有属性和方法
print '----dir----'

print dir('123')
print dir(123)

print len('ABC')  # 在len函数的内部调用的是__len__()方法
print 'ABC'.__len__();

# 演示len()方法
print '演示len()方法'


class myCls(object):
    def __len__(self):
        return 100;


cc = myCls();

print '-->', cc.__len__()

print '-->', len(cc)


# 操作对象的状态
print '获取对象状态'
# getattr(),setattr(),hasattr()
class myobj(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def mopt(self, x):
        return x * x;

obj1=myobj('naruto','man')
print hasattr(obj1,'name')
print hasattr(obj1,'sex')
# 设置属性
setattr(obj1,'age',19)  # 为当前对象设置一个新的属性age并为age赋值19
print obj1.age

# 获取属性
print getattr(obj1,'gender')
print getattr(obj1,'name')
print getattr(obj1,'sex','not_found')  # 获取不存在的sex属性，如果没有找到就返回not_found
print getattr(obj1,'hello','not_found')  # 获取不存在的sex属性，如果没有找到就返回not_found

# 将对象方法赋给变量
fn=getattr(obj1,'mopt')
print fn(5)