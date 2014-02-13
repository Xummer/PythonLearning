#!/usr/bin/python
# -*- coding: utf-8 -*
# Filename : func_default.py

# 只有在形参表末尾的那些参数可以有默认参数值，
# 即你不能在声明函数形参的时候，先声明有默认值
# 的形参而后声明没有默认值的形参。
#
# 这是因为赋给形参的值是根据位置而赋值的。
# 例如，def func(a, b=5)是有效的，
# 但是def func(a=5, b)是 无效 的。

def say(message, times = 1):
  print message * times

say('Hello')
Hello = 'Name'
say(Hello)
say('World', 2)
