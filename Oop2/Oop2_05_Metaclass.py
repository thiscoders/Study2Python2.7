# coding=utf-8
# !/usr/bin/env python2.7

print ''

'''
我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
type()函数既可以返回一个对象的类型，又可以创建出新的类型
比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义
'''


def fn(self, name='world'):
    print 'hello ' + name


'''
class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''
# 调用type()函数创建类的对象
Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()

h.hello()

print '----mateclass----'
'''
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
当我们定义了类之后就可以根据metaclass创建实例
如何创建出类？ 必须通过metaclass创建出类
连接起来就是：先定义metaclass，再创建类，再创建实例。可以把类看成metaclass的实例
'''


# metaclass是创建类，所以必须从type派生
class ListMetaclass(type):
    # 参数列表：当前准备创建的类的对象；类的名字；类继承的父类集合；类的方法集合
    def __new__(cls, name, bases, attrs):
        print 'ListMetaclass __new__ is running...'
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list):
    #  关键语句： 这句话指示python解释器在创建MyList的时候要通过ListMetaclass的__new__()来创建实例
    __metaclass__ = ListMetaclass


ml = MyList()
ml.add(1)
print ml

# 正常情况修改一个类只需要直接在类中加方法，通过metaclass修改纯属变态

# so,什么时候使用metaclass呢？当我们编写orm框架的时候
# 由于任务进度影响，这个点后续再加上
# todo

