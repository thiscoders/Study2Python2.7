## **PYTHON2.7基础知识**

***
### 一. 基础的IO操作
- 输入
    * num = raw_input('prompt')
- 输出
    * print '',''
**需要注意的是在每一个py文件的第一行添加文件编码方式**
```python
# 下面是python的示例代码，设置文件编码很重要
# coding=utf-8
# python code tode dosomething

# begin coding...
```

***

### 二. python的数据类型

|1|2|3|4|5|6|7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:| 
|整数|浮点数|字符串|布尔值|空值None|变量|常量|

***

### 三. 字符编码
* ord('A'): 将A转化为数字表示65
* chr(65): 将65转化为A显示
* len('abc'): 获取字符串长度
* Unicode表示的字符串用u'...'表示
* 'abc'.encode('utf-8'): 字符串'abc'转化为UTF-8编码，当然也可以是其他的编码方式
* 解决乱码问题
```python
# 为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
#! /usr/bin/env python
# 为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码
# -*- coding: utf-8 -*-
print 'code begin...'
```

***

### 四. 列表(list)和元组(tuple)
#### 1. list
```python
list=['a','b']
list.append('') # 尾部添加元素
list.insert('',6) # 指定位置添加元素
list.pop() # 删除行尾元素
list.pop(2) # 删除指定位置元素
list.sort() # 排序
```
#### 2. tuple
* 元组一旦定义就不能修改其中的元素
* 元组没有增删改方法，获取元素的方法和列表一致
* 只有一个元素的tuple必须在元素后面加一个,用来消除歧义 如： btuple = (1,)
 
***

### 五. python流程控制
#### 1. 分支结构
```python
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
```

#### 2. 循环结构
```python
# 1.for循环
for inum in range(start,end):
    # do somethings
# 2.while循环
while 条件:
    # do somethings
```

***

### 六. Dict&Set
#### 1. Dict(字典):保存键值对，类似java的map数据类型，并且key的值可以重复
- 赋值：dict[key]=value
    * 注意:如果Key不存在，那么该键值对会添加到字典中
- 取值：value=dict[key]  或者 value=dict.get(key,def)
    * 注意：如果key不存在，那么dict会报错
- 删除: dict.remove(key)
    * 注意：dict内部存放的顺序和key放入的顺序是没有关系的
#### 2. Set(集合)：用来存储单个元素，可以看成是数学意义上的无序和无意义的元素的集合，可以进行交并补操作
- 添加： set.add(value) #可以重复添加，但是没有意义
- 删除： set.remove(value) #删除不存在的元素就会报错
*  s1 = set([1, 2, 3]) # 集合的定义方式，容易忘记写set关键字

***

### 七. Function
#### 1. 函数
* 定义函数时，需要确定函数名和参数个数；
* 如果有必要，可以先对参数的数据类型做检查；
* 函数体内部可以用return随时返回函数结果；
* 函数执行完毕也没有return语句时，自动return None。
* 函数可以同时返回多个值，但其实就是一个tuple。
> **注意：在编写Python代码时如果可以设计成一个不变对象那就尽量设计成一个不变的对象**

***

### 八. 函数参数(Parameter Of Function)
#### 1. 必选参数
#### 2. 默认参数
- 注意默认参数有一个大坑，作为默认参数必须指向不变的对象,默认函数修改之后如下
```python
def def_func(a,num=None):
    if num is None:
        num=100
    # 'do something!'
```
- 如果默认参数不指向不变的对象，那么程序就会产生逻辑错误
#### 3. 可变参数
- *args表示可变参数，可变参数在函数的内部组装成了tuple
- 可变参数可以通过*()或者*[]的方式进行传参，比如：fun(*(1,2,3)),fun(*[1,2,3])
#### 4. 关键字参数
- **kw表示关键字参数，关键字参数在函数的内部组装成了dict
- 关键字参数可以通过\*\*dict的方式进行传参，比如: fun(\*\*{'name':'naruto','age':19})
#### 5. 注意事项
* 可变参数和关键字参数应该放在参数列表的尾部
* 参数顺序： 必选参数-->默认参数-->可变参数-->关键字参数
* 使用*args表示可变参数，**kw表示关键字参数是python的习惯写法，也可以换用其他，但是建议不要这么做
    
***
### 九. python的高级特性
#### 1. 切片：取出列表或者元组中的片段
1. list[0:10] 截取前10个元素 简写  list[:10]
2. list[-10,0] 截取最后10个元素 ，-1表示最后一个元素 简写 list[-10:] 
3. list[x,y] 截取第x到y个元素，包括x但是不包括y
4. list[x,y,s] x到y的元素，每s个元素取出第一个，如果要取出第二个元素，记住x+1修改其实位置
5. list[:] 截取整个列表，即复制列表
6. 字符串，元组均可切片
* **注意：不是所有的数据类型都可以进行切片**
* **注意：其实切片也支持倒数切片**
#### 2. 迭代：获取可迭代对象的值
##### a. 迭代字符串
##### b. 迭代列表
* list实现下标输出,list本身是没有下标的
```python
list=[1,2,3,4,5]
for num,val in enumerate(list):
    print num,val
```
##### c. 迭代元组
##### d. 迭代字典 dict.iteritems()获取词典的key和val
```python
dict={'key':'val','key':'val'}
for key,val in dict.iteritems():
    print key,val
```
##### e. for循环里同时引用两个变量
```python
for key,val in [('a':'1'),('b':'2'),('c':'3')]:
    print key,val
```
* 注意：不是所有对象都可以进行迭代，被迭代的对象必须是可迭代的对象
* 判断对象是否是可迭代对象：isinstance(obj, Iterable)
            
#### 3. 列表生成式： 按照一定的规律生成列表
##### a. 定义方法
1. list=range(1,100)
2. list=[x for x in range(1,100)]  # 同第一个 这个x是可以调用其本身的所有方法的
3. list=[x*x for x in range(1,100)]  #计算1-100所有数的平方
4. list=[x*x for x in range(1,100) if x%2==0] #筛选出偶数的平方 
5. list=[m+n for m in 'ABC' for n in '123'] #嵌套定义生成全排列
##### b. 列表取值
1. 调用next()方法 ,这种方法可以用但是很不推荐，如果列表中的元素有n多个，那么next()就要调用n多次
2. 使用for循环进行迭代, 这才是比较常规的做法
##### c. 判断某一个对象是否是某一种类型
```python   
isinstance(obj,type)
```
#### 4. 生成器： 是对列表生成器的一种优化，只在每一次调用next()的时候动态的在内存中进行计算，所以比较节省空间
##### a. 定义方法
1. gen=(x for x in range(1,20)) #逻辑比较简单的生成器,只是将列表生成器的[]改成了()括号           
2. 逻辑非常复杂的生成器需要借助函数进行改造
```python
#定义生成器
def fib(max):
    n,a,b=0,0,1  
    while n < max:
        yield n,b   
        a,b=b,a+b
        n=n+1
    # 使用生成器
    for val in fib(6):
        print val
```                
> 注意：生成器的特点--> 每一次调用生成器的next()方法的时候，
> 程序会执行到yiele就返回,下次调用next()的时候就会从yield处继续执行下去
> 直到遇到return或者函数体执行完毕就是生成器的结束指令(generator) 
##### b. 取值： 生成器取值和列表生成式是一致的，不建议使用next(),推荐使用for循环迭代
* 注意： 生成器迭代到最后一个元素的时候如果继续迭代就会抛出StopIteration的错误
                