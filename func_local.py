#!/usr/bin/python
# -*- coding: utf-8 -*
# Filename : func_local.py

#只是传值，x为局部变量
def func(x):
  print 'x is', x
  x = 2
  print 'Changed local x to', x

x = 50
func(x)
print 'x is still', x
