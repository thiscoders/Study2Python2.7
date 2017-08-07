# coding=utf-8
# !/usr/bin/env python2.7

# 函数参数的学习
# 1. 默认参数
def defParam(num=100):
    return num;


print defParam(10);  # 如果调用函数的时候向函数传递了参数，那么该参数就是你传递的值
print defParam();  # 如果在调用函数的时候没有给一个参数具体的值，那么该参数就是默认的值


def registerDoc(name, gender, age=18, country='中国'):
    print 'name=', name, ',gender=', gender, ',ang=', age, ',country=', country;


registerDoc('naruto', '男');  # 使用默认参数
registerDoc('Sasuke', '男', 19);  # 传递第一个默认参数，第二个默认参数country将会保持不变
registerDoc('Sakura', '女', country='Japan');  # 使用第二个默认参数，第一个将会保持不变  -->  即不按顺序提供默认参数


# 2.默认参数有利也有弊，使用不当就会掉进沟里，例如：
def add_end(L=[]):  # 函数的作用：传递一个列表，该函数向列表的尾部添加end
    L.append('end');
    return L;


print add_end([1, 2]);  # 当传递一个正常的列表是该函数执行的结果是正确的，符合预期的

# 接下来传递一个空的list作为参数
print add_end();
print add_end();
print add_end();


# 正确的执行结果是每一次调用都只打印一个end
# 然而执行结果却是随着调用的增多，end打印的也越多

# 注意：接下来解释这是为什么：在上面的默认参数定义中，默认参数L其实是一个变量，每一个调用add_end()是都会改变L的值，所以L的end会一直增加
# 因此 在编码中尽量使用不变的对象，--> 定义默认参数牢记一点，默认参数必须指向不变的对象
# 使用不变对象的好处
# ①.不变对象一旦定义就不能修改，这就减少了由于修改数据而导致的错误
# ②.多任务环境下同时读取对象不用加锁
# 对函数进行修改如下
def add_end(L=None):
    if L is None:
        L = [];
    L.append('end');
    return L;


# 3.可变参数:
# a.什么是可变参数： 可变参数就是指函数传递参数的时候即可以传递一个参数，也可以传递多个参数，最终参数会在函数内部组装成一个tuple
def calc_sum(*num):  # 在函数的内部参数num接受到的是一个元组，注意：是一个元组  and  一定要加一个星号，一个，一个，一个
    isum = 0;
    for i in num:
        isum = isum + i;
    return isum;


print calc_sum();
print calc_sum(3, 5);
print calc_sum(1, 2, 3, 22, 11);


# 可变参数只能放在参数列表的最后一个位置，否则会引起语义的二义性
def sum_calc2(a1, a2, *nums):
    a1 = a1 + a2;
    for i in nums:
        a1 = a1 + i;
    return a1;


# b. 问题：如果参数本身就包含列表或者元组该怎么办？
li = [1, 2, 3, 5];
tu = (5, 1);
print calc_sum(*li);
print calc_sum(*tu);


# 通过在列表或者元组前面加上*，让其变成可变参数
# 注意，元组和列表不可以同时变成可变参数传递进去,比如： calc_sum(*tu,*li);
# print calc_sum(*li,1,2); 这种形式也是不可以的


# 4. 关键字参数
# a.什么是关键字参数： 函数允许传递>=0个含参数名的参数，这些关键字参数会在函数内部自动的组装后成一个dict
# 注意，关键字参数只能放在参数列表的最后，否则会引起语法的二重性
def key_fun(name, age, **kw):
    print name, age, kw;


key_fun('naruto', 18, gender='man', country='woodleaf');

# b.可以先组装出一个dict，再将dict作为关键字参数传递到function中
adict = {'gender': 'man', 'country': 'woodleaf', 'hobby': 'lamian'};
key_fun('Sasuke', 19, **adict);


# 5.一个神奇的函数
def magical_fun(num1, num2=None, *args, **kw):
    if num2 is None:
        num2 = 100;
    print 'num1=', num1, ',num2=', num2, ',args=', args, ',kw=', kw;


# 第一个参数
magical_fun(12);
# 参数全写
magical_fun(1, 12, *['a', 'b', 'c'], **{'name': 'naruto', 'age': 18});

# 照此看来，任何一个函数都可以写成形如fun(*args,**kw)的形式,即--> 任何函数都可以通过tuple和dict来调用
print  abs(*[-100]);

# 例子如下
def func01():
    print 'func01';


def func02(num1, num2):
    print 'res', num1, num2;


func01(*[]);
func02(*[1, 2]);


# 6.编写递归函数
def fact(num):
    if num == 1:
        return 1;
    return num * fact(num - 1);


print fact(3);


# a.递归函数优化
def fact1(n):
    return fact_iter(n, 1);


def fact_iter(num, product):
    if num == 1:
        return product;
    return fact_iter(num - 1, num * product);

# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
