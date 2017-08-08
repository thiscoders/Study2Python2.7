# coding=utf-8
# !/usr/bin/env python2.7

# 自定义异常
class WhatException(RuntimeError):
	def __init__(self,arg):
		self.args=arg


def execFunc(num):
	if(num<10):
		raise WhatException('RuntimeErrorOccu')
	return num*2


def callFunc():
	try:
		print execFunc(2)
	except "Num Error",e:
		print 'errorrrr',e.args
	finally:
		print 'finallyyy'

callFunc()
