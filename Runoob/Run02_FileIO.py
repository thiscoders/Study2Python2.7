# coding=utf-8
# !/usr/bin/env python2.7

#while True:
# 接收键盘输入
#    hel = raw_input("please input ")       
#    if hel=='q':
#        break
#    print 'lala...',hel
#print 'this is the end...'
import os
print "文件IO"
print os.getcwd()
# 从根目录开始
fo=open('./Runoob/res/res.txt')
# fo.read() 函数读取文件内容
#content=fo.read()
print fo.tell() # 获取当前指针位置
content=fo.read(20) # 读取文件的前20个字符
print content
print fo.tell()
fo.seek(0)  # 指针定位
content=fo.read(50) # 读取文件的前20个字符
print content


#os 模块
# os.rename(filename)
# os.remove(filename)
# os.mkdir(path)
# os.rmdir(path) 删除目录
# os.chdir(path) 改变当前目录
# os.getcwd()


