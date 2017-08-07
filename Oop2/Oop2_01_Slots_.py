# coding=utf-8
# !/usr/bin/env python2.7

from types import MethodType


class person():
    pass


p1 = person()
# 尝试给实例绑定属性
p1.name = 'xiaoming'
p1.gender = 'man'
print p1.name, ' ', p1.gender


def func(self, name):
    print 'hello I\'m', name


# 尝试给实例绑定方法
p1.sayhello = MethodType(func, p1, person)
p1.sayhello('mack')

p2=person()
# print p2.sayhello() # 报错
''' 上述给实例绑定方法，对另一个实例是不起作用的，要对所有实例起作用，需要在程序运行过程中动态的给class加上功能，语法如下 '''
person.sayhello2=MethodType(func,None,person)

p2.sayhello2('jihua')

p1.sayhello2('wanghua')

''' 在开发中，有时候还需要限制class可以绑定的属性，这个时候就需要使用__slots__ '''
print '----使用__slots__限制类可以绑定的属性----'
# 只允许student类添加name和age属性
class student(object):  # 如果不继承于object那么__slots__就不起作用
    __slots__=('name','age')
    pass

s1=student()
s1.name='tom'
s1.age=18
print s1.name,s1.age

s2=student()
#s2.score=59 # 报错，因为score不在__slots__元组中
#print s2.score
''' __slots__只对当前类有效，对其继承子类是无效的，除非在子类中也定义__slots__,这样子类允许定义的属性就是自身的__slots_
    加上父类的__slots__
'''
class erha(student):
    __slots__ = ('score');

eh=erha();
eh.name='husky'
eh.age=6
eh.score=57

print eh.name,eh.age,eh.score

# eh.gender='nani'  #报错，＿slots__不存在这个属性



