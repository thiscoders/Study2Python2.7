### **OOP面向对象编程一**
***
#### 一. Python类的格式
```python
class student(object):
    # 类似java的构造函数
    def __init__(self, name):
        self.name = name;

    def func(self):
        print 'func is running...'
```
***
#### 二. 继承与多态
```python
# subclass继承自student
class subclass(student):
    def func(self):
        print 'student func is running...'

```

***

###  三. 获取对象信息
#### 1. 判断对象类型
* type(obj,type_name)   # 返回对象类型
    1. type(123)  ==> <type 'int'> 
    2. type('123')  ==> <type 'str'> 
* isinstance(obj,class_name) # 判断对象是否是某一个类的实例，或某一个类子类的实例
    1. isinstance('123', str)  ==> True 
    2. isinstance('123', int)  ==> False
* isinstance(obj,(class_name,...)) # 判断对象是否是n多对象中的一个
    1. isinstance(u'123', (str, unicode)) ==> True  
#### 2. 判断对象是否存在某一个属性
* hasattr(obj,'age') : 判断obj对象中是否存在age属性
#### 3. 设置对象属性
* setattr(obj,'age',19) : 向对象obj设置新的属性age=19,但是该方法只对当前obj生效
#### 4. 获取对象属性
* getattr(obj,'sex') : 获取obj的sex属性，如果找不到这个属性python解释器就会报错
* getattr(obj,'sex','not_found') : 获取obj的sex属性，如果找不到这个属性python解释器就会返回not_found (写什么就返回什么，这里写了not_found就返回not_found)
* 上述方法也可以获取函数
#### 5. 可以将对象的函数赋值给某一个变量
```python
fn=getattr(obj,'func')  
# 执行
fn(param...) 
```
***    
### 四. 封装、继承和多态===>>多重继承、定制类、元类
* 数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。
* 接下来会讨论多重继承、定制类、元类等概念。
    