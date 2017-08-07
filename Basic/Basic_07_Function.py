# coding=utf-8
# !/usr/bin/env python2.7

# 学习函数
# 1.调用函数：调用函数需要注意函数名字的写法和参数个数以及参数类型(重要)，也有必要注意一下函数的返回值
# 常用函数
print abs(-100);  # 取绝对值

print cmp(1, 2), cmp(2, 1), cmp(1, 1);  # 比较函数

print float('12.76');

print unicode('abc');

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs;
print a(-20);


# 2.定义函数
def sayHello(who):  # 定义一个有返回值的函数
    if who is None:
        print '请输入你的名字';
    else:
        print '你好,', who;
        return '函数返回值';  # 这是函数的返回值


print sayHello('Naruto');  # 如果函数没有返回值，那么此处会打印None


# pass : 这是一个占位符，如果没有想好函数的内容要怎么写，可以先用这个关键字占位
def passFun():
    pass;
    if True:
        print 'Hello';


# 3.完善一个关于函数的小例子，自定义绝对值函数
def mabs(num):
    # 判断num的类型是否正确
    if not isinstance(num, (int, float)):
        print '你输入的参数类型是不对的！';
        raise TypeError('错误的参数类型');
    if num < 0:
        return num * (-1);
    else:
        return num;


print mabs(12);


# 4.函数返回多个值 ,注意，其实python的多个返回值返回的只是一个元组
def mutliRes():
    return 1, 2, 3, 4;


a1, b1, c1, d1 = mutliRes();

print a1, b1, c1, d1;
d = mutliRes();
print d;  # 多个返回值只是python的一种障眼法，其实只返回了一个元组，而只有一个元素的元组是可以省略括号的，所以只有一个返回值的函数我们是看不到括号的
# 如果函数执行到末尾仍然没有return那就默认返回None
