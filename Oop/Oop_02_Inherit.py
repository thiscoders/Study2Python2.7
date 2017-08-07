# coding=utf-8
# /usr/bin/env python2.7

# 继承与多态
# 1.继承
# 定义man作为父类
class man(object):
    def run(self):
        print 'man can running...'

    def whosyoudaddy(self):
        print 'my daddy is man!!!'


# 定义spuerman作为子类,重写run方法
class superman(man):
    def run(self):
        print 'superman can fly...'


class ironman(man):
    def run(self):
        print 'ironman is cool...';


m1 = man()
sm1 = superman()

m1.run()
sm1.run()
m1.whosyoudaddy()
sm1.whosyoudaddy()

print '----isinstance----'
# isinstance()方法判断变量是不是某个类型
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
print 'm1 is man?', isinstance(m1, man)
print 'm1 is spuerman?', isinstance(m1, superman)  # 父类不是子类的类型
print 'sm1 is spuerman?', isinstance(sm1, superman)
print 'sm1 is man?', isinstance(sm1, man)

# 但是任何子类都是父类的类型
im1 = ironman();
im1.whosyoudaddy()
print '----多态----'


# 2.多态
# 这个方法只可以接受man类型，以及man的子类
def showMutli(man):
    man.run();


# 调用showMutli方法
showMutli(m1)
showMutli(sm1)
showMutli(im1)

'''
由运行结果可见调用的都是showMutli()方法，但是由于传递的对象不同因此执行结果也不相同，这就是多态
'''
