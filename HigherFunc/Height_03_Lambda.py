# coding=utf-8
# !/usr/bin/env python2.7

# lambda: 匿名函数 : 顾名思义，没有名字的函数
# 1. 用于map/reduce函数,列表各项平方
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6]);

'''
lambda x:x*x
=
def func(x):
    :return x*x;

匿名函数限制：
    匿名函数只能用一个表达式，其返回值就是表达式的结果

匿名函数没有名字，所以不用担心函数名冲突
匿名函数也是一个对象，所以也可以将匿名函数赋值给一个变量，再利用变量来调用函数
'''

print '-------------';


# 匿名函数做返回函数
def get_lambda(x):
    return lambda x: x / 2;


print get_lambda(10);  # <function <lambda> at 0x02E3B7F0>
func1 = get_lambda(10);
print func1;  # <function <lambda> at 0x02E3B7F0>
# print func1(); # 报错： TypeError: <lambda>() takes exactly 1 argument (0 given)
print func1(12);  # 6


# 匿名函数访问父函数的参数
def mpower(num):
    return num * num;


def father(ok, *x):
    def inner(*x):  # 访问不到father的x，因为只会访问到inner的x，如果调用时不传递这个x就会报错
        return map(mpower, x);

    def inner2():  # 可以访问到father的x，因为inner2的x不存在
        return map(mpower, x);

    def inner3(info):  # 即访问到inner3的info又可以访问到father的x
        return ['lala...' + info, map(mpower, x)];

    if int(ok) == 1:
        return inner;
    elif int(ok) == 2:
        return inner2;
    else:
        return inner3;


pm = father(2, *[1, 2, 3, 4, 5]);
print pm();

pmt = father(3, *[1, 2, 3, 4, 5]);
print pmt('hello');


# 使匿名函数使用父函数的参数方法如下
def father2(*x):
    return lambda: map(mpower, x);


pm2 = father2(*[1, 2, 3]);
print pm2();  # [1, 4, 9]
