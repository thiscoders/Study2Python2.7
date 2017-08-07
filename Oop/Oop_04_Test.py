# coding=utf-8
# !/usr/bin/env python2.7

class ninjia(object):
    def __init__(self, name):
        self.name = name

    def func(self):
        print 'func is running...'

    def setscore(self,score):
        self.score=score

    def getscore(self):
        return self.score


naruto=ninjia('naruto')
naruto.func()
naruto.setscore(87)
print naruto.getscore()

''' 编写get/set方法的作用 '''
# 在传递参数的时候对参数进行校验

