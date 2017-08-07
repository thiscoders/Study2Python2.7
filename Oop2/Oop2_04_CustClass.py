# coding=utf-8
# !/usr/bin/env python2.7
# 导入正则模块
import re

print '定制类'

# 1. __str__
print '__str__'


class Naruto(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):  # print Natuto('001')  ==>  naruto:001   这样打印出来的字符不仅好看，而且容易打印出实例内部的数据
        return 'naruto:' + self._name

    # 直接打印n调用__repr__, print n 调用__str__
    __repr__ = __str__


n = Naruto('001')

print n

n

# 2. __iter__  如果一个类想要被用于for..in..循环，类似list或tuple那样。就必须实现__iter__方法
# 这个方法返回一个迭代对象，然后for循环就会不断调用该迭代对象的next()对象，直到遇到StopIteration错误退出循环
print '__iter__'


class Fib(object):
    def __init__(self):
        self.a, self.b = 1, 1

    # 实现__iter__()方法，以便于for循环迭代
    def __iter__(self):
        return self

    # 实现next()方法
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a


for val in Fib():
    print val

# 3. __getitem__ 可以将对象当做列表使用,即可以被切片
print '__getitem__'


class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b;
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            l = []
            for x in range(stop):
                if x >= start:
                    l.append(x)
                a, b = b, a + b
            return l;


f2 = Fib2();
print f2[1:8]

# 4. __getattr__   当调用类中不存在的属性的时候可以调用该方法
print '__getattr__'


class Student(object):
    def __init__(self):
        self.name = 'this name'

    # 当调用的属性或者函数不存在的时候，python解释器会试图调用
    def __getattr__(self, item):
        if item == 'score':
            return 'Hello world,this is score...'
        elif item == 'desc':
            return lambda: '你好，this is func'


s = Student()
print s.name  # 获取存在的属性
print s.score  # 获取不存在的属性
print s.score1  # 获取__getattr__()中也不存在的属性，如果没有就返回None
print s.desc()


# 只让类响应几个特定的属性
class Stu01(object):
    def __getattr__(self, item):
        if item == 'aaa':
            print 'aaa'
        elif item == 'bbb':
            print '222'
        else:
            raise AttributeError('参数不存在');


s2 = Stu01()
s2.bbb


# 链式调用
class ChainCall(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        # 返回了一个新的对象,这样就可以继续调用方法了
        return ChainCall('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path


cc = ChainCall()
# 这就是github网站API的结构  https://github.com/thiscoders?tab=repositories
# 无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
print cc.user.hello.world.abc


#  练习一： 写出这样的链式调用 Chain().users('michael').repos
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        if path == 'users(.)':
            print 'hello'
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path


c1 = Chain()
print c1.aaa.user

# 5. __call__
print '__call__'


class Teacher(object):
    def __init__(self, name):
        self._name = name

    def __call__(self, *args, **kwargs):
        print 'hello ' + self._name
        print args, kwargs


t1 = Teacher('小李')
t1(1, 2, 3)

# 6.判断对象能否被调用
print callable(t1)
print callable(123)
