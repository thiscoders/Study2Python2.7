# coding=utf-8
# !/usr/bin/env python2.7
import functools;

# decorator
print '--------装饰器--------';


# 1.需求一：在函数now调用之前打印日志
def supernow(func):
    def inner(*args, **kw):
        print '%s is called!' % func.__name__;
        return func(*args, **kw);

    return inner;


# 基础函数，打印时间
@supernow
def now():
    print '2017-03-12';


# 重要： 上述@语法的写法等效于 now=spuernow(now);

now();

print '----自定义日志内容----';


# 需求二：在函数now调用之前打印自定义日志
# 自定义打印日志的内容
def spuernow2(logcon):
    def subnow2(func):
        def newnow2(*args, **kw):
            print func.__name__ + ' is called!' + logcon;
            return func(*args, **kw);

        return newnow2;

    return subnow2;


# 基础函数
@spuernow2('啦啦')
def now2():
    print '2017-03-12 13:00';


# 重要：上述@语法相当于: now2=spuernow2('text')(now2);  此处好好理解

now2();

# 再次复习一次
print '----复习----'


def log2(text):
    # 这个log1函数相当于没有自定义日志的装饰器
    def log1(func):
        def agent(*args, **kw):
            print '日志...哈哈哈..' + text;
            return func(*args, **kw);

        return agent;

    return log1;


@log2('呵呵呵呵和')
def now3():
    print 'this is now333!';


now3();

print '函数名：' + now3.__name__;  # 经过装饰器的函数其__name__属性已经变了，这会使一些依赖函数签名的代码出错

# 一个完整的装饰器示例，带函数签名修改
print '----perfact----';


def sayHello(who):
    def subfunc(func):
        # 等效于agent.__name__=func.__name__ ,这就解决了函数签名的问题,但是这样做太low，所以用@语法比较高大上
        @functools.wraps(func)
        def agent(*args, **kw):
            print who;
            return func(*args, **kw);

        return agent;

    return subfunc;


@sayHello('lihua')
def hello():
    print 'hello';


hello();

print '函数名：' + hello.__name__;

print '--------练习--------'


# 练习一:编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志,并且还能接收返回值
def spuerlog(func):
    @functools.wraps(func)
    def agent(*args, **kw):  # 这个函数已经开始返回执行结果，也就是固定的值了，它返回的不是函数
        print 'begin call';
        res = func(*args, **kw);
        print 'end call';
        return res;

    return agent;


@spuerlog
def func01():
    print 'func01 is running...';
    return 100;


print func01();

# 练习二: 编写一个decorator，使它即能支持@decor,又能支持@decor('info')

print '----练习2----';


def spuerlog2(*info):
    def sublog2(func):
        @functools.wraps(func)
        def agent(*args, **kw):
            if len(info) != 0:
                # 将列表转化为字符串输出
                print reduce(lambda x, y: x + y, info);
            return func(*args, **kw);

        return agent;

    return sublog2;


@spuerlog2('hello001', ' world!')
def func02():
    print 'func02 is running...';


func02();

@spuerlog2()
def func03():
    print 'func03 is running...';

func03();