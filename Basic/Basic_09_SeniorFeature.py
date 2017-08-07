# coding=utf-8

# !/usr/bin/env python2.7
# 导入外部包
import os
from collections import Iterable

print 'Python 高级特性'

print '---1.切片---'
# 1.切片 : 取一个List或者Tuple的一部分
alist = ['aa', 'bb', 'cc', 1, 2, 3]
print alist[0:3]  # 获取0,1,2 ,前闭后开区间
print alist[:3]  # 第一个0可以省略不写
# python支持L[-1]取倒数第一个元素，那么它同样支持切片倒数
print alist[-5:-3]  # 输出bb,cc

# a.创建出一个数字序列
nums = range(100)
# aa.取前10个数
print nums[:10]
# ab.取后10个数
print nums[-10:]
# ac.取50->60之间的数字
print nums[50:60]
# ad.前10个数，每两个取一个数
print nums[:10:2]
# * 取第二个元素时需要定基准
print 'haha', nums[1:10:2]
# af.所有数每5个取一个
print nums[::5]
# ag.什么都不写，那就赋值出一个lists
print nums[:]

# 重要：tuple和string都可以使用切片操作
# 元组切片之后仍然是元组
atuple = (1, 2, 3, 4, 5, 6, 7)
print atuple[:3]
print atuple[:6:3]
# 字符串切片之后仍然是字符串
str1 = 'abcdefghigklmnopqrst'
print str1[0:10]
print str1[:10:2]
# 注意：想要获取别的元素更改切片起点就可以了



print '---2.迭代---'
# 2.迭代
# python允许迭代任何可以迭代的对象，通过collections模块的Iterable类型可以判断当前对象是否可以迭代，
# Python内置的enumerate函数可以把list变成索引-元素对
# a.迭代list
print 'list:'
blist = ['a1', 'a2', 'a3', 'b1', 'b2']
for val in blist:
    print val

# b.迭代元组
print 'tuple:'
btuple = (1, 2, 3, 'a', 'b', 'c')
for val in btuple:
    print val

# c.迭代字符串
print 'string:'
str2 = 'hello'
for val in str2:
    print val

# d.甚至可以迭代字典
print 'dict:'
bdict = {'a': 1, 'b': 2, 'c': 3, 'd': 'hello'}
for key in bdict:
    print key
# d1.同时迭代字典的key和value
for key, val in bdict.iteritems():
    print key, ' : ', val

# d2.判断对象是否是一个可以迭代的对象
atest = 'abs'  # 可迭代
btest = 12  # 不可迭代
print isinstance(atest, Iterable)
print isinstance(btest, Iterable)

# c.对list实现下标循环
print 'list:'
clist = ['a', 'b', 'c', 'd']
for key, val in enumerate(clist):
    print key, val

# d.for循环里面同时引用两个变量
for x, y in [('a', 1), ('b', 2), ('c', 3)]:
    print '(', x, ',', y, ')'

# 任何可迭代对象都可以使用for循环


print '---3.列表生成器---'
# 3.生成指定的列表
print range(1, 10)
# a.生成每一个数字的平方的列表
print [x * x
       for x in range(1, 10)]

# b.for后面还可以加上if判断，从而筛选出偶数的平方
print [x * x for x in range(1, 20) if x % 2 == 0]

# c.两层嵌套循环生成全排列
print [m + n for m in 'abc' for n in '123']

# d. 列出当前目录下所有文件和目录名
print [d for d in os.listdir('.')]

# e. 列表生成式可以使用两个变量生成list
dd = {'a': '1', 'b': '2', 'c': '3'}
print [k + '=' + v for k, v in dd.iteritems()]

# f.将list的所有字符串变成小写
ll = ['AAA', 'Bbb', 'Ced']
print [s.lower() for s in ll]

# *.判断一个变量是不是字符串
print isinstance('abs', str)
print isinstance(123, str)

# 4.生成式
print '---4.生成器---'
# a.生成器存在的意义
# 列表生成式需要占用大量的内存空间，使用生成器只在每一个调用next()方法或者每一次迭代的时候才会动态的计算出下一个值，
# 这样就极大的节省了内存空间
# b.生成器的第一种定义方式generator
print [x for x in range(1, 10)]  # 列表生成式
gen01 = (x for x in range(1, 10))  # 定义generator： 注意generator保存的是算法，所以占用内存空间比较小
for val in range(1, 10):
    print gen01.next()  # 每一次调用next就会动态计算出下一个值,然而看法中很少这么用
# 最后一个元素被输出之后再调用next()方法就会抛出StopIteration错误

# 开发中对生成器进行迭代使用for循环
gen02 = (x for x in range(20, 30))
for val in gen02:
    print val


# 对于逻辑非常复杂的生成器(列表生成式写不出来的)可以使用函数
# 斐波那契数列生成式
def fib(max):
    i = 0
    a = 0
    b = 1
    while i < max:
        print i, '--->', b
        a, b = b, a + b  # 注意理解
        i = i + 1


fib(8)


# 将上述函数可以改成生成器
def gen_fib(max):
    i = 0
    a = 0
    b = 1
    while i < max:
        yield i, b
        a, b = b, a + b  # 注意理解
        i = i + 1


fib1 = gen_fib(5)
print fib1.next()
print fib1.next()
print fib1.next()
print fib1.next()
print fib1.next()


def gen_fib2(max):
    i = 0
    a = 0
    b = 1
    while i < max:
        yield i, b
        a, b = b, a + b  # 注意理解
        i = i + 1


for val in gen_fib2(8):
    print 'aaa', val


# 解释变成生成器的函数
# 普通的函数会一直执行到函数的尾部，执行中间如果遇到return就返回
# 而生成器的函数在调用next()方法的时候，每一次执行到yield就返回，再次执行的时候就会从yield处继续执行,直到遇到retuen或者执行到函数的末尾generatot就会执行结束
# 接下来验证这一点

def vali_gen():
    yield 'aaa'
    yield 'bbb'
    yield 'ccc'


avali = vali_gen()
print avali.next()
print avali.next()
print avali.next()
# print avali.next()

# 改成迭代器的函数执行遇到return或者执行到函数的末尾就是generator的结束指令
# 所有的生成器都基本上不会用next()来调用，几乎都会使用for来迭代
