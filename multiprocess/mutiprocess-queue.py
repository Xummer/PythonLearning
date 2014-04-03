#!/usr/bin/env python
# -*- coding: utf-8 -*
# Filename : mutiprocess-queue.py

import os
import multiprocessing
import time

q_max_size = 3

# input worker
def inputQ(queue):
	info = str(os.getpid()) + '(put):' + str(time.time())
	queue.put(info)

# output worker
def outputQ(queue, lock):
	info = queue.get()
	lock.acquire()
	print (str(os.getpid()) + '(get:)' + info)
	lock.release()

# Main
record1 = []	# store input process
record2 = []	# store output process
lock = multiprocessing.Lock()	# to prevent messy print
queue = multiprocessing.Queue(q_max_size)

# input process
for i in range(10):
	process = multiprocessing.Process(target=inputQ, args=(queue,))
	process.start()
	record1.append(process)

# output process
for i in range(10):
	process = multiprocessing.Process(target=outputQ, args=(queue, lock))
	process.start()
	record2.append(process)

for p in record1:
	p.join()

queue.close()	# No more object will come, close the queue

for p in record2:
	p.join()
