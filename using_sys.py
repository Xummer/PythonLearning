#!/usr/bin/python
# -*- coding: utf-8 -*
# Filename : using_sys.py

import sys

print 'The commend line arguments are:'
for i in sys.argv:
  print i

print '\n\nThe PYTHONPATH is', sys.path, '\n'
