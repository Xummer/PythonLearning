#!/usr/bin/env python
# -*- coding: utf-8 -*
# Filename : exception.py

import sys

def test(n):
	try:
		if n % 2:
			raise Exception("Error Message!")
	except Exception, e:
		print "Exception:", e.message
	else:
		print "Else..."
	finally:
		print "Finally..."

test(1)

test(2)