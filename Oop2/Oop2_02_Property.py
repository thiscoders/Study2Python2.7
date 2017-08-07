# coding=utf-8
# !/usr/bin/env python2.7

print 'property'
'''
使用set/get方法非常繁琐
@property 装饰器负责把方法变成一个属性，这样调用起来就会比较方便
'''


class student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        if not isinstance(val, int):
            raise ValueError('you input not is int...')
        if int(val) < 0 or int(val) > 100:
            raise ValueError('you input num shiould bweteen 0 and 100')
        self._score = val

    @score.getter
    def score(self):
        print 'getter is running...'
        return self._score;


# 定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

s1 = student()
s1.score = 87
print s1.score


class Teacher(object):
    def __init__(self):
        print '初始化...'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if val == 'aaa':
            print 'please input again'
            return
        self._name = val

    @name.getter
    def name(self):
        return self._name


t1 = Teacher()
t1.name = 'wangming'
print t1.name
