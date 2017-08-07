# coding=utf-8
# 设置编码方式防止显示乱码
# !/usr/bin/env python2.7

# 1.输出
print 'Hello world!', '你好', 'lala';
print 300 + 200;
print '300 + 200 =', 300 + 200;

# 2.输入
# 注意raw_input()返回的永远是字符串，所以用这个函数输入的数字相加永远是字符串之间的连接,除非用int()函数转化返回结果
name = raw_input('请输入名字：');
print '你的名字是', name;


