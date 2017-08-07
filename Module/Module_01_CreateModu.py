# coding=utf-8
# !/usr/bin/env python2.7


'这是文档注释，可以使用__doc__来访问，任何模块代码的第一个字符串都被视为模块的文档注释'

__author__ = 'ye';  # 模块作者

import sys;

# 导入模块的使用别名
try:
    # 导入cString别名为StringIO
    import cStringIO as StringIO;
except ImportError:  # 捕获异常
    import StringIO;

try:
    import json;
except ImportError:
    import simplejson as json;


# 由于python是动态语言，函数签名一致接口就一样，因此无论导入那个模块后续代码都能正常工作





def test():
    # sys.argv 用list存储了命令行所有参数， argv的第一个参数永远都是该python文件的名称
    args = sys.argv;
    if len(args) == 1:
        print 'Hello world!';
    elif len(args) == 2:
        print 'Hello ' + args[1];
    else:
        print 'you param too mach,', args;


# 当在终端里面运行模块的时候，python将特殊变量__name__置为__main__,而在其他地方导入该模块的时候，if判断将会失败，因此，这种if测试可以让一个模块
# 通过命令运行一些额外的代码，最常见的是运行测试
if __name__ == '__main__':
    test();

# 所用域
'''
python的作用域： 仅希望在模块的内部使用通过_前缀来实现
                正常的函数和变量名是公开的，可以被直接引用
                类似__xxx__的变量是特殊变量，可以被直接饮用但是有特殊用途，比如上述__author__和__name__,文档注释可以用__ doc__访问，自己的变量不要用这种变量名
                类似_xxx和__xxx这样的函数或者变量就是非公开的(private)，不应该被直接引用，其实非要引用也可以，但是编程习惯上不应该引用private的函数和变量
'''


# 私有变量的用途
def _private_1(name):
    print 'hello', name;


def _private_2(name):
    print 'lala,%s' % name;


def greeting(name, num):
    if num == 1:
        return _private_1(name);
    else:
        return _private_2(name);

greeting('liuye',2);

# 我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来，这样在调用greeting()函数的时候就不用关心内部的private函数细节，这
# 也是一种非常有用的代码封装和抽象的方法。注意：编程时，外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义成public
