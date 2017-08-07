# coding=utf-8
# !/usr/bin/env python2.7

print '--------返回函数--------';


# 1.函数作为返回值,列表求和
def lazy_sum(*args):
    def inner_func():
        ax = 0;
        for val in args:
            ax = ax + val;
        return ax;

    return inner_func;


# 当调用lazy_sum()的时候，返回的并不是求和结果，而是求和函数，注意：此时求和函数并没有执行
sum1 = lazy_sum(*[1, 2, 3, 4, 5, 6, 7]);
# 此处：当调用求和函数的时候才真正计算求和结果
print sum1, sum1();

'''
闭包：在上述例子中，在函数lazy_sum内部有定义了inner_func, 内部函数inner_func可以引用外部函数lazy_sum的参数和局部变量,
当lazy_sum返回inner_func的时候，相关参数和变量都保存在返回的函数中，这种程序结构就是“闭包”。
闭包是一个很重要的概念，必须好好掌握
'''

sum2 = lazy_sum(*[1, 2, 3, 4, 5, 6, 7]);
# 注意：每一次调用lazy_sum函数的时候，尽管参数相同，但是，每一次都会返回新的函数。所以闭包返回的函数都不再是同一个对象
print sum1 == sum2;  # 参数相同，但是返回值是不相同的

'''
def outer_func(*args):
    field01;
    def inner_func():
        # 内部函数inner_func可以引用外部函数outer_func的参数和变量
        ...do something
    # 当outer_func返回inner_func的时候，inner_func所引用的外部参数和变量全部保存在返回的函数中
    (注意：保存在返回的函数中，而每一个返回函数又是一个新的对象)，
    return inner_func;


闭包解释：当outer_func函数被调用的时候返回了inner_func，此时inner_func并没有被执行，那么什么时候执行inner_func呢？那就
是当调用inner_func的时候它才会执行
'''


def count():
    # 定义一个列表，保存函数
    fs = [];
    for val in range(1, 4):  # for循环 1，2,3
        def inner_func():  # 函数计算val的平方
            return val * val;

        # 将inner_func添加到fs中
        fs.append(inner_func);
    # 此时fs中已经包含了3个函数，现在，将其作为返回值返回
    return fs;


f1, f2, f3 = count();
print f1();  # 9
print f2();  # 9
print f3();  # 9

'''
1.按照正常的思路预期执行结果：上面的f1,f2,f3的返回结果应该分别是1,4,9。即当调用count的时候每次for循环时inner_func也执行
    了。这种思路下的代码执行逻辑如下：当调用count()函数的时候，count函数的for循环启动，第一次向fs中添加函数的时候val=1，
    此时inner_func返回的就是1。第二次向fs中添加函数的时候val=2，此时inner_func返回的就是4。以此类推，下一个就是9。
    OK，记住。这种想法是错误的，正确的返回结果是9,9,9。

2.正确结果的解释：当调用count的时候每一次for循环inner_func并没有执行，当第一次向fs中添加元素的时候val=1，然而函数inner_func
    并没有执行，所以返回1这种情况就无从谈起，同样对于for接下来的循环也可以用同样的方式进行解释。而当调用f1的时候才开始执行
    inner_func，而此时val的值已经变成了3.所以执行结果是9，9，9。这一点可以用断点调试来验证

注意：返回闭包的时候必须牢记，返回函数不要引用任何循环变量，也不要引用任何后续会变化的变量，否则程序的执行结果可能会出乎你的意料

进阶：除非可以让程序的效率成千上万倍增加，否则必须严格遵守上面的注意

'''


# 2. 如果非要在返回函数中使用循环变量，那就在创建一个函数，这个函数的参数绑定当前循环变量的值，一旦绑定便不能修改，所以，对count函数修改如下
def count2():
    fs = [];
    for val in range(1, 4):
        def outer(num):  # num参数一旦传递进来就不能改变,因为这个函数并不是返回函数，所以这个函数在count调用的时候就已经执行了
            print 'outer';

            def inner():
                print 'inner;'
                return num * num;

            return inner;

        fs.append(outer(val));  # 向outer传递val参数
    return fs;


# 这个函数解决的返回函数引用循环变量的问题，但是缺点是代码太长，可以使用lambda函数来缩短代码


f11, f12, f13 = count2();

print f11();
print f12();
print f13();
