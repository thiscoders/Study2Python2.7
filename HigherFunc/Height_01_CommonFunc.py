# coding=utf-8
# !/usr/bin/env python2.7

print '--------高阶函数--------';

print '1.map/reduce';
'''
    1.什么是序列：列表,元组,字符串,Unicode字符串,buffer对象,xrange对象
    2.python中的容器分为：序列(例如列表和元组)和映射(例如字典)
    3.序列的通用操作
        1.索引,2分片,3加,4乘(重复),5成员资格（检查某个元素是否属于序列的成员）
        6计算序列长度(内建函数),7最大元素(内建函数),8最小元素(内建函数)
'''


# 1.map: map传入的参数有两个，参数一：函数，参数二：序列
#        map 函数的作用：map将传入的函数一次作用到序列的每一个元素，并把结果作为新的序列返回


# a.计算一个列表每个的平方并且将平方作为新列表的元素并且返回
def mpower(num):  # 函数，这是map的第一个参数
    return num * num;


alist = [2, 4, 6, 8, 10];  # 列表，这是map的第二个参数
print map(mpower, alist);  # 调用map进行计算

# b.将list的所有数字转化为字符串
blist = [1, 2, 3, 4, 5, 6, 7];
print map(str, blist);

# 2. reduce : reduce 必须接受两个参数，函数和序列
#             reduce 把结果继续和序列的下一个元素做累积运算： reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4) 个人认为这是将f做递归运算

# a.序列求和,1-->100数列求和
clist = range(1, 101);


def msum(x, y):
    return x + y;


print reduce(msum, clist);

# b.将序列[1,3,5,7,9]变成13579
dlist = [1, 3, 5, 7, 9];


def fn(x, y):
    return x * 10 + y;


print reduce(fn, dlist);


# c.定义一个函数，将string转化为int ,map和reduce配合使用
def str2num(s):
    def fn(x, y):
        return x * 10 + y;

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s];

    return reduce(fn, map(char2num, s));


print str2num('87345') + 10;


# d.使用lambda
def str2num2(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    def str2int(s):
        return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# 关于lambda函数在后面就会讲到

# print str2num2('10') + 10;


# 练习一：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# iteritems:同时迭代字典的key和value
# hsooe fesfuwe erfewrf
def formatstr(s):
    alist = list(s);
    alist[0] = alist[0].upper();

    def mupper(s):
        return s.lower();

    res = alist[0] + ''.join(map(mupper, s[1:]));
    return res;


print formatstr('HELLO');


# 练习二：编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(li):
    def multi(x, y):
        return x * y;

    return reduce(multi, li);


print prod([10, 2, 3, 4, 5, 6, 2, 3, 2]);

# 3.filter : python内建的函数filter()用于过滤序列 ，其关键在于如何实现一个筛选函数
# filter()接收两个参数，第一个是函数，第二个是序列filter将序列的每一个元素作用于函数，根据函数的返回值是True还是False决定是不是保留这个元素
# 比如：去掉一个序列中所有的奇数，只留下偶数
elist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];


def filterNum(num):
    if num % 2 == 0:
        return True;
    return False;


# 只保留偶数
print filter(filterNum, elist);


# 4. 排序函数sorted() : 这个函数同样接收两个参数，第一个参数是函数，第二个参数就是一个序列
# python 规定  a>b返回1，a=b返回0，a<b返回-1 ，因此我们就可以自定义排序函数，比如倒序排序
# 自定义排序函数
def reversed_com(x, y):
    if x < y:
        return 1;
    elif x == y:
        return 0;
    else:
        return -1;


# 定义序列
glist = [1, 9, 7, 4, 5, 6];
print sorted(glist, reversed_com);

# 常规的正序排序
print sorted(glist);


# 高阶函数的抽象能力是非常强大的，所以，应该尽量将核心代码写的尽可能的简洁，这样代码就会比较容易阅读
