#!/usr/bin/python
# -*- coding: utf-8 -*
# Filename : using_sys.py

import sys

#print
print 'name: ' + 'xummer'
#print会依次打印每个字符串，遇到逗号“,”会输出一个空格
print 'hoby: ' , 'game'
print 'one argument %s' % '1' 
print 'two argument %s and %d' % ('1', 1)

#print用r'' 表示''中的字符不转译
print r'\n 2333 \t\n'

#print 用'''...'''来简化\\\n换行


#sys
print 'The commend line arguments are:'
for i in sys.argv:
  print i

print '\n\nThe PYTHONPATH is', sys.path, '\n'
