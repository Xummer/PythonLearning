#!/usr/bin/env python
# -*- coding: utf-8 -*
# Filename : poolresult.py

import multiprocessing, time

def func(msg):
	time.sleep(.5)
	if len(msg) > 0:
		print str(time.time())+msg
		return 0
	else:
		return 1

if __name__ == '__main__':
	pool = multiprocessing.Pool(3)
	results = []
	for i in xrange(3):
		msg = "hellow %d" % i
		p = pool.apply_async(func, (msg, ))
		results.append(p)

	while True:
		for idx, res in enumerate(results):
			if res.get() == 0:
				msg = "hellow %d" % idx
				p = pool.apply_async(func, (msg, ))
				results[idx] = p
	
	#pool.close()
	#pool.join()
