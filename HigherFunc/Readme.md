## **高阶函数**
### 将函数作为参数传入这样的函数叫做高阶函数，当然高阶函数也可以返回函数
***

### 基础知识部分的补充：
#### 1.什么是序列：列表,元组,字符串,Unicode字符串,buffer对象,xrange对象
#### 2.python中的容器分为：序列(例如列表和元组)和映射(例如字典)
#### 3.序列的通用操作

|1|2|3|4|5|6|7|8|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|索引|分片|加|乘(重复)|成员资格(检查某个元素是否属于序列的成员)|计算序列长度(内建函数)|最大元素(内建函数)|最小元素(内建函数)|

***

## **开始高阶函数**

***

### 一. 常用的高阶函数
#### 1. map
- map(func,seq):将函数作用于seq的每一个元素，并且将结果组成一个新的List返回
#### 2. reduce
- reduce(func,[x1,x2,x3,x4])=func(func(func(x1,x2),x3),x4)
#### 3. filter(func,seq)
- 将函数作用于序列的每一个元素。根据函数的返回值来确定元素的去留
#### 4. sorted(seq,func): 
- func决定了序列的排序方式，倒序排列，正序排列，自定义顺序...

***

### 二. 返回函数
#### 1. 返回函数是高阶函数的特性之一：指的是一个函数可以将函数作为返回值返回
- 代码形式如下，这种代码结构被称为闭包
```python
def outer_func(*args):
    field=1;
    def inner_func():
        opt field;#...
        opt args;#...
        # do something...
    return inner_func;
```
#### 2. 关于参数的作用域
```python
def father(ok, *x):
    def inner(*x):  # 访问不到father的x，因为只会访问到inner的x，如果调用时不传递这个x就会报错
        return map(lambda x:x*x, x);

    def inner2():  # 可以访问到father的x，因为inner2的x不存在
        return map(lambda x:x*x, x);

    def inner3(info):  # 即访问到inner3的info又可以访问到father的x
        return ['lala...' + info, map(lambda x:x*x, x)];
```
#### 注意：
1. 返回函数inner_func可以引用outer_func的参数args和变量field
2. 当调用outer_func的时候inner_func并不会立即执行
3. 当调用inner_func的时候inner_func才会执行
4. 返回函数不要引用任何循环变量以及任何后续会发生变化的变量

***

### 三. 匿名函数 顾名思义：没有名字的函数(lamdba)
1. 定义方式以及含义：
```python
lambda x:x*x
# 等效于==> 
def func(x):
    return x*x
```
2. 匿名函数只能用一个表达式，返回值就是表达式的结果

***

### 四. 装饰器(decorator)
#### 1. 什么是装饰器：增强函数功能的高级函数，返回值也可以是函数
#### 2. 案例一：函数调用之前打印日志
```python
import functools;
def spuerhello(func):
    @functools.wraps(func)  # 解决函数签名依赖问题
    def agent(*args,**kw):
        print 'log here...';
        func(*args,**kw);

@superhello
def hello():
    print 'hello';

# 上面的写法等效于 hello=superhello(hello)

```

#### 3. 案例二：函数调用之前打印自定义日志

```python
import functools;
def spuerhello(log):
    def subhello(func):
        @functools.wraps(func)
        def agent(*args,**kw):
            print log; # 此处打印自定义log
            return func(*args,**kw);
        return agent;
    return subhello;

@superhello('logcon')
def hello():
    print 'hello';
# 上面的写法等效于superhello('logcon')(hello)

```
### 五. 偏函数(functools.partial)
#### 1. 什么是偏函数: 当函数的参数过多，调用麻烦的时候，需要化简，可以使用functools.partial创建一个新的函数，这个新的函数可以固定住原函数的部分参数，从而化简调用
#### 2. 定义以及含义解释
```python
import functools;
int2=functools.partial(int,base=2);
# 相当于
def int2(x,base=2): # 将关键字参数base写死了
    return int(x,base);
```
#### 3. 注意：所有的偏函数均可以写成如下形式
    functools.partial(fun_name,*args,**kw);

