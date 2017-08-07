# coding=utf-8
# !/usr/bin/env python2.7

# python多重继承
class Runnable(object):
    def run(self):
        print 'i can run...'

class Flyable(object):
    def fly(self):
        print 'i can fly...'


class SuperMan(Runnable,Flyable):
    pass;

s1=SuperMan()
s1.run()
s1.fly()

