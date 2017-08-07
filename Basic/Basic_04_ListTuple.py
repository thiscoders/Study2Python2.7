# coding=utf-8
# !/usr/bin/env python2.7

# 1.list：列表，python内置的一种数据类型，list是一种有序集合可以随时添加和删除其中的元素
alist = ['aaa', 'bbb', 'ccc', 'ddd', 123];
# a.打印list
print 'a', alist;

# b.获取list中元素的个数
print 'b', len(alist);

# c.用索引来访问每一个位置的元素,下标从0开始
print 'c', alist[0], alist[3];
print 'c', alist[-1], alist[-4];  # alist[-x] 可以倒叙获取元素，最后一个元素的下标是-1

# d.list尾部追加元素
alist.append('222');
print 'd', '添加元素之后，len=', len(alist);

# e.list 指定位置插入元素
alist.insert(1, '111');
print 'e', alist;

# f.删除尾部元素
alist.pop();
print 'f', alist;

# g.删除指定位置的元素
alist.pop(1);  # 可以输入负数进行删除
print 'g', alist;

# h.替换元素
alist[1] = 'Hello';
print 'h', alist;

# i.二维列表，即列表中的元素还是列表
alist.append(['me', 'you', 'he']);
print 'i', alist;
# j.获取二维列表的数据
print alist[5][0];

print '-----------------------------------------------------';
# 2.tuple: 元组，tuple和list非常相似，但是tuple一旦初始化就不能修改,元组没有append，insert这样的方法，但是取元素的方法和list一样
atuple = ('111', '222', 'you');
print atuple;

print atuple[1];

# 注意：只有一个元素的tuple必须在元素后面加一个,用来消除歧义 如： btuple = (1,);
print (1);
print (1,);

# *.一个有趣的元组
funtuple = ('a', 'b', [1, 2, 3]);
print funtuple;
print funtuple[2][1];
funtuple[2][1] = 18;
print funtuple;
# 注意： 2变成了18，说明了元组并非元素不变，所谓的不变指的是每一个元素的指针指向永远不变


