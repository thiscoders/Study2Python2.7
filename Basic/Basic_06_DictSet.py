# coding=utf-8
# !/usr/bin/env python2.7

# 字典(Dict)和集合(Set)

# 1.什么是字典 ,字典相当于java中的map数据类型，其中保存的是 键-值 对，是一种牺牲空间换取时间的做法
# 字典的key必须保证不变，可以使用字符串，整数等，列表就不可以用来作为key
adict = {'aaa': 111, 'bbb': 222};
print adict['bbb'];

adict['bbb'] = 'Hello';
print adict['bbb'];  # 多次对一个key放入value后面的值会覆盖前面的值

# a.给key赋值的时候如果key不存在那么dict就会将其添加到字典中
adict['lala'] = 1;
print adict;

# b.取值的时候key不存在dict就会报错
# print adict['hehe'];

# c.为了python代码的健壮性，在取值的时候判断key是否存在 ,在学习异常处理之前暂时采用这个方法
# 方法有两种
# 方法一 ： 通过in判断key是否存在
print '方法一:', 'aaa' in adict, ' and ', 'hehe' in adict;
# 方法二： 通过dict提供的get方法，如果key不存在则返回None或者返回自己定义的值
print '方法二:', adict.get('aaa'), ' ', adict.get('hehe'), ' ', adict.get('hehe', -100);

# d.删除一个key，使用dict.pop('key'); 这个方法会同时删除key对应的value
print adict;
adict.pop('lala');
print adict;

# 注意：dict内部存放的顺序和key放入的顺序是没有关系的
# dict 的key可以重复
bdict = {'aaa': 123, 'bbb': 456, 'aaa': 789};  # 这种写法很不推荐，因为最后一个aaa所对应的值会覆盖第一个aaa所对应的值
print bdict;

# 2.set 集合和dict类似但是不存储value，在set中key是不能重复的
# set可以看成数学意义上的无序和无重复元素的集合，所以，set可以做数学上的交并补操作
aset = set(['a1', 'b1', 'c1', 'c1']);
print aset;

# a.添加元素,可以重复添加但是不会有效果
aset.add('12');
aset.add('12');
print aset;
# b.删除元素,重复删除元素会报错
aset.remove('a1');

print aset;

# set的交并补操作
s1 = set([1, 2, 3]);
s2 = set([3, 4, 5]);
print '交集', s1 & s2;
print '并集', s1 | s2;
print '差集', s1 - s2;

# 注意；调用不变对象自身的任意方法，也永远不会改变该对象自身的内容，而会创建新的对象并且返回
s1 = 'abc';
s2 = s1.replace('a', 'B');
print s1, s2;

print '---TEST---';
# 测试:试试把(1, 2, 3)和(1, [2, 3])放入dict或set,有助于理解dict和set
tdict1 = {'aaa': (1, 2, 3)};  # this ok,因为dict的key对用的value本身就是可变的
tdict2 = {'aaa': (1, [2, 3])};  # this ok,因为dict的key对用的value本身就是可变的
print tdict1['aaa'];
print tdict2['aaa'];

tset1 = set([(1, 2, 3), 2]);  # this ok,因为元组的内容是不可变的
print tset1;
# tset2 = set([(1, [2, 3])]);  # 这是不可行的，因为列表的数据是可变的 形如set([(1, [a, b],[c,d])])的集合，因为a,b,c,d的值是不确定的，所以并不能保证集合里面的元素不重复
# print tset2;
