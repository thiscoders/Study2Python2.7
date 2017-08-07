# coding=utf-8
# !/usr/bin/env python2.7

import functools;

print '----偏函数----';

print int('1011010001', base=2);

# 当参数的个数太多的时候，需要简化，可以使用functools.partial创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，使函数调用更加简单
int2 = functools.partial(int, base=2);

print int2('11100');

'''
int2 = functools.partial(int, base=2);
相当于
def int2(x,base=2):
    return int(x,base);
'''

# 上述例子中仅仅是把base参数固定住了，但是也可以在调用的时候传入其他值
print int2('123', base=10);

# 注意：functools.partial可以表达为这种形式functools.partial(func_name,*args,**kw)
int3 = functools.partial(int, '1110', base=2);  # func_name=int   args=[1110]  kw={base=2}
print int3();

max1 = functools.partial(max, 10);  # 相当于max(1,5,3,10); 即args=[1,5,3,10]
print max1(1, 5, 3);
