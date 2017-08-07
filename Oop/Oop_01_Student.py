# coding=utf-8
# !/usr/bin/env python2.7

# 创建一个student类
class student(object):
    # 这样写__init__()方法需要传3个参数name,score和school。self参数是由解释器自动传递
    def __init__(self, name, score, school):
        self.name = name;
        self.score = score;
        self.school = school;

    # 定义在类中的方法和普通的方法只有一点不同，那就是在类中的方法必须有一个self参数并且该参数是第一个参数
    # 调用的时候不用传递这个参数，但是仍然可以出传递默认参数，可变参数和关键字参数
    def descSelf(self):
        print 'name is ' + self.name, ',score is ' + str(self.score), ',school is ' + self.school;


# 为student创建一个对象
liming = student('liming', 78, 'xian shiyou daxue');

# 调用liming的descSelf()方法
liming.descSelf();
# 设置liming的名字为小李
liming.name = '小李';
# 再次调用descSelf()方法发现liming的name已经变成小李
liming.descSelf();
