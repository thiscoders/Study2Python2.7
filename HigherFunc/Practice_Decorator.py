# coding=utf-8
# !/usr/bin/env python2.7

import functools

def deco_time(func):
	def inner(*args,**kw):
		print 'what...'
		return func(*args,**kw)
	return inner

@deco_time
def mnow():
	print 'hello'

mnow()
