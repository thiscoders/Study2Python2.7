# coding=utf-8
# !/usr/bin/env python2.7
import time
import functools

print '____装饰器练习____'

print '________基本装饰器________'


def timerFunc(func):
    start = time.time()
    print 'start is ', start
    func()
    end = time.time()
    print 'end is ', end
    print 'the time is ', end - start
    # return lambda x : x*x


@timerFunc
def func():
    # a = raw_input('你说好咱就走:')
    # print '', a
    print 'hello'


# 调用被装饰的函数 形如@xxx
func

print '________被装饰的函数带参数________'


def decFunc2(func):
    print 'decFunc2 is running...'

    @functools.wraps(func)  # 将返回函数的函数名改成原函数，解决函数签名的问题
    def subfunc(*args, **kw):
        print 'subfunc is running...'
        return func(*args, **kw)

    return subfunc


@decFunc2  # func2(who)=decFunc2(who)
def func2(who='lihua'):
    print 'say hello to ', who


print 'return func name is ', func2.__name__  # 返回函数名
# func2('janny')

# 3 函数传递参数，以及装饰器本身也需要参数怎么办
print '________带参数的装饰器________'


def decFunc3(*content):
    print 'decFunc3 is running...'

    def innerFunc(func):
        print 'innerfunc is running...'

        def subFunc(*args, **kw):
            print 'subFunc is running...', content
            return func(*args, **kw)

        return subFunc

    return innerFunc


@decFunc3('aaa', 'bbb', 1, 2, 3)  # func3(**)=decFunc3('aa','bb')(**)
def func3(num1, num2):
    print num1, '*', num2, '=', num1 * num2


f = func3
f(6, 7)

# 4. 多重装饰
print '________多重装饰________'


def decGoodbye1(func):
    def subFunc(*args, **kw):
        print 'subFunc1 is running...'
        func(*args, **kw)

    return subFunc


def decGoodbye2(func):
    def subFunc(*args, **kw):
        print 'subFunc2 is running...'
        func(*args, **kw)

    return subFunc


def decGoodbye3(func):
    def subFunc(*args, **kw):
        print 'subFunc3 is running...'
        func(*args, **kw)

    return subFunc


@decGoodbye1
@decGoodbye2
@decGoodbye3
def goodbye(who):
    print 'goodbye', who


goodbye('Janny')

