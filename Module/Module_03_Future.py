# coding=utf-8
# !/usr/bin/env python2.7

# python提供了__future__模块，将下一个版本的新特性导入到当前版本，于是我们就可以在当前版本中测试一些新版本的特性

from __future__ import unicode_literals
from __future__ import division

print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)

print '*************************'

print '10 / 3 =', 10 / 3
print '10.0 / 3 =', 10.0 / 3
print '10 // 3 =', 10 // 3
