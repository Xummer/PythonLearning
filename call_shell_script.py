#!/usr/bin/python
# -*- coding: utf-8 -*
# Filename : call_shell_script.py

import os
print os.name

pwd = os.getcwd()
shscript = 'test.sh'
shpath = pwd + '/' + shscript
print shpath

# first method
n = os.system(shpath)
print n

# second method
# os.popen(shpath)
