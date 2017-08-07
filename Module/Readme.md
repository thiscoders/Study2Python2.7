### **模块**

***

#### 一. 模块的标准格式
```python
# coding=utf-8
# !/usr/bin/env python2.7

'这是一个完整的python Module代码的描述部分，这一部分是对当前模块进行描述的'

__author__ = 'author_name'

import sys;

_pri = 100  # 私有变量

# 私有函数
def _pri_func():
    print 'pri_func is running...';


def func():
    print 'hello world!', _pri
    _pri_func()

# 当在终端里面运行模块的时候，python将特殊变量__name__置为__main__,而在其他地方导入该模块的时候，if判断将会失败，因此，这种if测试可以让一个模块通过命令运行一些额外的代码，最常见的是运行测试
if __name__ == '__main__':
    print '__name__ is running...'
    func()

```

***
#### 二. 安装第三方模块
    * Python有两个封装了setuptools的包管理工具：easy_install和pip
    * pip install module_name
    * easy_install 不推荐使用
    
***
#### 三. 使用__future__模块，可以在当前版本中测试新版本的一些特性
```python
from __future__ import division

# ..do something

```



