### 面向对象高级编程
***
#### 1. 使用__slots__
    1. 定义
        ```python
         class man(object):
             __slots__=('name','gender')
             pass;
         class superman(man):
             __slots__ = ('from')
             pass;
        ```
    2. __solts__使用规律
        * 使用__slots__的类必须继承自object，否则__slots__属性无效
        * __slots__只对当前的类生效，对其继承子类不会生效
        * 如果__slots__的类有继承子类且子类有__slots__属性，那么子类允许定义的属性就是自身的__slots__加上父类的__slots__ 
        
***
#### 2. 使用@properties
    1. 定义
      ```python
        class Person(object):

            @properties
            def score(self): 
                # 注意： 此处必须是_score属性，否则会报错
                return self._score

            @score.setting
            def score(self,val):
                # ...数据校验
                self._score=val

            @score.getting
            def score(self):
                # ...do something
                return self._score;
      ```
    2. setting , getting , del 并不是全都要选的
    
#### 3. 多重继承
1. 语法
```python

class SuperMan(Runnable,Flyable):
    pass;
```
***
#### 4. 自定义类
1. \_\_str\_\_  : p=person()  p==> 调用__str__()方法
2. \_\_iter\_\_ : 使对象可以被迭代
3. \_\_getitem\_\_ : 使对象可以使用list的相关属性，比如切片
4. \_\_getattr\_\_ : 获取对象不存在的属性或者方法，并且也可以用于链式调用
5. \_\_call\_\_ : p=person() p()==> 调用__call__()方法
***
#### 5. type()&metaclass
1. 创建对象 type()函数
2. metaclass 修改类的结构



