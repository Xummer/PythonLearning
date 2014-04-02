#!/usr/bin/env python
# -*- coding: utf-8 -*
# Filename : process_pool.py

import multiprocessing as mul

def f(x):
	return x ** 2

pool = mul.Pool(5)
rel = pool.map(f, [1,2,3,4,5,6,7,8,9,10])
print(rel)